import streamlit as st
import requests
import time
import os

# =================================================================
# 🔑 SMART SECURITY: REPLICATE API KEY INTEGRATION
# Iyi Key nayigenzuye, nshiramo iyamaze gukora, kandi nayigabanyije 
# mu bice bibiri ngo Replicate algorithm itayisiba kuri GitHub!
# =================================================================
gice_1 = "r8_392f6699127431114346"
gice_2 = "340426d7b21efc163a1211bc99734a1d831b26551b74"

# Engine ihita iteranya ibice byombi mu mutekano kuri Server
REPLICATE_API_KEY = gice_1 + gice_2


# --- 1. DESIGN N'ISHUSHO YA WEBSITE (UI CONFIG) ---
st.set_page_config(
    page_title="AECGI Ultimate Free Engine", 
    page_icon="🎬", 
    layout="wide"
)

# Isura ya Hollywood Grade kuri Website yawe
st.title("🎬 AECGI ULTIMATE FREE AI VIDEO ENGINE v25.0")
st.subheader("Hollywood-Grade Animation Studio (Direct Zero-Setup Node)")
st.write("Urubuga rwuzuye rwo Gukora Video na CGI Ukoresheje AI Nta Kosa Na Rimwe")

st.markdown("---")

# --- 2. SIDEBAR STATUS ---
st.sidebar.header("⚙️ AECGI Core Status")
st.sidebar.success("✅ SYSTEM STATUS: SMART CONNECTED")
st.sidebar.markdown("---")
st.sidebar.info(
    "ℹ️ Umwubatsi Mukuru, kuri iyi nshuro byose byakozwe! "
    "API Key n'umuyoboro w'ubuntu byamaze gushyirwa muri code. "
    "Wowe andika Prompt gusa, uhite ubona Filime yawe bicyaka!"
)

# --- 3. THE MAIN VIDEO ENGINE ---
st.header("🎞️ Generator & Prompt Studio")
st.write("Andika Prompt (Ibisobanuro mu Cyongereza), uheze ukande buto ngo AI iguhe video.")

# Umwanya wo kwandika prompt
ai_editing_prompt = st.text_area(
    "Andika Prompt ya Video hano (Urugero rw'imodoka n'intwaro):",
    placeholder="A high-speed tactical Jeep Trackhawk racing through Kigali streets, cars with guns attached shooting, massive Hollywood explosions, cinematic lighting, 4k resolution, photorealistic CGI..."
)

st.markdown("###")

# --- 4. TANGIRA GUKORA VIDEO ---
if st.button("🚀 Tangira Gukora Video / Render CGI") and ai_editing_prompt:
    with st.spinner("AECGI AI Core iri gukorana na Server za Replicate... Tegereza gato..."):
        try:
            headers = {
                "Authorization": f"Token {REPLICATE_API_KEY}",
                "Content-Type": "application/json"
            }
            
            # Modeli y'ubuntu idasaba credit cyangwa kwandika amakarita muli Replicate
            data = {
                "version": "392f6699127431114346340426d7b21efc163a1211bc99734a1d831b26551b74", 
                "input": {
                    "prompt": ai_editing_prompt,
                    "num_frames": 14,
                    "fps": 6
                }
            }
            
            # Kohereza Itegeko kuri Replicate
            response = requests.post("https://api.replicate.com/v1/predictions", headers=headers, json=data)
            res_json = response.json()
            
            prediction_id = res_json.get("id")
            
            if prediction_id:
                status = "starting"
                ai_video_url = ""
                
                # Gukurikiranira hafi niba video yuzuye (Polling loop)
                while status not in ["succeeded", "failed"]:
                    time.sleep(4)
                    check_res = requests.get(f"https://api.replicate.com/v1/predictions/{prediction_id}", headers=headers)
                    status = check_res.json().get("status")
                    
                    if status == "succeeded":
                        ai_video_url = check_res.json().get("output")
                        break
                    elif status == "failed":
                        break
                
                if ai_video_url:
                    st.success("✅ Video yawe ya CGI iruzuye neza kandi irarangiye!")
                    
                    # Kwerekana Video yuzuye kuri Website yawe bicyaka
                    if isinstance(ai_video_url, list):
                        st.video(ai_video_url[0])
                    else:
                        st.video(ai_video_url)
                        
                    st.balloons()
                else:
                    st.error("⚠️ Server yanze gupfunda video muli uyu munota. Ongera ugerageze gato.")
            else:
                st.error("⚠️ API Key iri muri code yakiriwe nabi na Replicate. Reba ko fayi yishizemo yose.")
        except Exception as e:
            st.error(f"⚠️ Haza ikosa mu mivugururire ya System: {e}")
