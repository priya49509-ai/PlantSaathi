import streamlit as st
from PIL import Image
from datetime import datetime

st.set_page_config(page_title="PlantSaathi | Plant Care Assistant", page_icon="🌱", layout="wide")

ISSUES = {
    "Yellow leaves": {
        "possible": "Overwatering, underwatering, or nutrient stress",
        "steps": ["Check the top 2–3 cm of soil before watering.", "Make sure the pot has drainage holes.", "Provide suitable indirect light.", "Check whether older or newer leaves are turning yellow."],
        "urgency": "Check watering and drainage first",
    },
    "Brown leaf tips or edges": {
        "possible": "Low humidity, irregular watering, or fertilizer/salt buildup",
        "steps": ["Water consistently without leaving the pot standing in water.", "Avoid adding extra fertilizer until the plant improves.", "Check whether mineral buildup may be a factor.", "Trim fully dry edges with clean scissors if desired."],
        "urgency": "Review watering consistency",
    },
    "Brown or black spots": {
        "possible": "Leaf-spot disease, sun damage, or water sitting on leaves",
        "steps": ["Keep affected leaves from touching healthy plants.", "Avoid wetting foliage when watering.", "Remove badly affected leaves with clean tools.", "Monitor whether spots spread."],
        "urgency": "Monitor whether spots spread",
    },
    "Wilting or drooping": {
        "possible": "Dry soil, waterlogged roots, heat stress, or transplant stress",
        "steps": ["Feel the soil before watering; both too little and too much water can cause wilting.", "Move the plant away from harsh afternoon sun while it recovers.", "Check drainage and look for a sour smell from waterlogged soil.", "Recheck after correcting the likely cause."],
        "urgency": "Check soil moisture before watering",
    },
    "White powder or cotton-like patches": {
        "possible": "Possible powdery mildew or mealybugs",
        "steps": ["Inspect stems and leaf undersides closely.", "Separate the plant from nearby plants while investigating.", "Check whether the material rubs off.", "Use only a treatment labelled for the identified pest or disease and plant."],
        "urgency": "Inspect carefully and isolate if spreading",
    },
    "Healthy / no visible symptoms": {
        "possible": "No obvious issue reported",
        "steps": ["Water according to the plant's needs and soil moisture.", "Provide suitable light.", "Check leaf undersides periodically for pests.", "Avoid over-fertilizing."],
        "urgency": "Continue routine care",
    },
}

PLANT_CARE = {
    "Money Plant / Pothos": ("Bright, indirect light; tolerates lower light.", "Water when the top few centimetres of soil feel dry.", "Avoid keeping roots constantly waterlogged."),
    "Tulsi / Holy Basil": ("Several hours of bright light or gentle sunlight.", "Water when the surface begins to dry; ensure good drainage.", "Pinch growing tips to encourage bushier growth."),
    "Aloe Vera": ("Bright light, with some direct sun after gradual adjustment.", "Let the soil dry well between waterings.", "Use a fast-draining potting mix and a pot with drainage."),
    "Snake Plant": ("Indirect light to some direct light; adaptable.", "Let soil dry substantially before watering again.", "Overwatering is a common cause of root problems."),
    "Rose": ("Usually needs several hours of direct sunlight.", "Water the soil deeply when needed; avoid constant sogginess.", "Provide airflow and inspect leaves for pests or spots."),
    "Tomato": ("Full sun, commonly at least 6–8 hours.", "Keep soil evenly moist, not waterlogged.", "Avoid large swings in soil moisture during fruit development."),
    "Other / Not sure": ("Check the specific plant's light requirements.", "Check soil moisture before watering rather than following a fixed schedule.", "Identify the plant if possible before using fertilizer or treatments."),
}

if "journal" not in st.session_state:
    st.session_state.journal = []

st.title("🌱 PlantSaathi")
st.subheader("A friendly plant-care assistant for beginners")
st.write("Upload a plant photo, describe what you notice, and get a simple care checklist. This college prototype uses symptom-based guidance; it does not diagnose disease from image pixels.")

with st.sidebar:
    st.header("🌿 Plant details")
    plant = st.selectbox("Choose your plant", list(PLANT_CARE))
    symptom = st.selectbox("What do you notice?", list(ISSUES))
    days = st.number_input("Days since you noticed it", min_value=0, max_value=365, value=1)
    environment = st.selectbox("Where is the plant kept?", ["Indoor", "Balcony", "Garden / outdoor", "Windowsill"])
    st.caption("Tip: check soil moisture before watering.")

tab1, tab2, tab3 = st.tabs(["🔎 Plant check", "🌼 Care guide", "📔 Plant journal"])

with tab1:
    left, right = st.columns(2)
    with left:
        st.markdown("### Add a plant photo")
        uploaded = st.file_uploader("Upload a leaf or whole-plant photo", type=["jpg", "jpeg", "png", "webp"])
        if uploaded:
            try:
                image = Image.open(uploaded).convert("RGB")
                st.image(image, caption="Uploaded plant photo", use_container_width=True)
            except Exception:
                st.error("Could not open that image. Try a JPG or PNG file.")
        else:
            st.info("A photo is optional. This version displays the image but does not classify it.")
        notes = st.text_area("Extra observations (optional)", placeholder="Example: soil is wet, plant is near a sunny window...", height=100)
    with right:
        st.markdown("### Your care assessment")
        result = ISSUES[symptom]
        st.markdown(f"**Reported symptom:** {symptom}")
        st.markdown(f"**Possible causes to consider:** {result['possible']}")
        st.warning(f"**First check:** {result['urgency']}")
        st.markdown("**Suggested next steps**")
        for item in result["steps"]:
            st.markdown(f"- {item}")
        st.caption("General educational guidance only, not a confirmed diagnosis. Consult a local horticulture expert if symptoms worsen.")
        if st.button("Save check to journal", type="primary", use_container_width=True):
            st.session_state.journal.append({
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "plant": plant, "symptom": symptom, "days": int(days),
                "environment": environment, "notes": notes.strip(),
                "possible_causes": result["possible"],
            })
            st.success("Saved to your session journal.")

with tab2:
    st.markdown(f"### Care basics: {plant}")
    light, water, tip = PLANT_CARE[plant]
    a, b = st.columns(2)
    with a:
        st.markdown("#### ☀️ Light")
        st.write(light)
        st.markdown("#### 💧 Water")
        st.write(water)
    with b:
        st.markdown("#### 🌱 Helpful tip")
        st.write(tip)
        st.markdown("#### 🧭 Environment")
        st.write(f"Selected location: **{environment}**")
    st.info("Care needs vary with season, pot size, soil, and local climate. Check the plant regularly.")

with tab3:
    st.markdown("### Your recent plant checks")
    if not st.session_state.journal:
        st.info("No checks saved yet. Go to Plant check and choose 'Save check to journal'.")
    else:
        for entry in reversed(st.session_state.journal):
            with st.expander(f"{entry['date']} · {entry['plant']} · {entry['symptom']}"):
                st.write("**Possible causes:**", entry["possible_causes"])
                st.write("**Environment:**", entry["environment"])
                st.write("**Days noticed:**", entry["days"])
                if entry["notes"]:
                    st.write("**Notes:**", entry["notes"])
        if st.button("Clear session journal"):
            st.session_state.journal = []
            st.rerun()

st.divider()
st.caption("PlantSaathi student prototype | Photo upload is for viewing only; no image-based ML model is bundled. Do not use this tool as the sole basis for chemical treatment or edible-crop safety decisions.")
