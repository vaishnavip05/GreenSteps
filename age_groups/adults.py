import streamlit as st
import json
from modules.scoring import scoring_ui, add_score
from modules.rewards import rewards_ui, add_points


def adults_dashboard():
    st.title("👨‍💼 Adults Zone")
    # ---------------- HOME BUTTON ----------------
    if st.button("🏠 Home"):
    st.session_state.page = "home"
    st.rerun()

    # ---------------- USER INFO ----------------
    st.write(f"Welcome, **{st.session_state.user}**")
    st.write("Awareness Level:", st.session_state.user_level)

    st.divider()

    # ---------------- PROGRESS ----------------
    scoring_ui()
    rewards_ui()

    st.divider()

    # ---------------- DAILY SUGGESTION ----------------
    st.subheader("🏠 Smart Home Suggestion")
    st.info(
        "Switching to LED bulbs can reduce energy consumption "
        "and lower your electricity bill."
    )

    if st.button("I will try this"):
        add_score(10)
        add_points(10)
        st.success("Great decision! +10 points 🌱")
        st.rerun()

    st.divider()

    # ---------------- AI DECISION STUDIO ----------------
    st.subheader("🧠 AI Decision Studio")

    # ✅ FIXED PATH
    with open("decision_studio/scenarios.json", "r") as f:
        scenarios = json.load(f)

    scenario = st.selectbox(
        "Choose a situation:",
        [s["title"] for s in scenarios]
    )

    selected = next(s for s in scenarios if s["title"] == scenario)

    option_names = [o["name"] for o in selected["options"]]
    choice = st.radio("What would you pick?", option_names)

    if st.button("Evaluate Decision"):
        option = next(o for o in selected["options"] if o["name"] == choice)

        impact = option["impact"]

        if impact > 0:
            st.success("Great eco-friendly decision! 🌱")
        else:
            st.error("This choice has environmental cost.")

        st.write(f"Impact score: {impact}")

        add_score(max(impact, 0))
        add_points(max(impact, 0))

    st.divider()

    # ---------------- MONEY DONATION ----------------
    st.subheader("🤝 Support a Cause")

    cause = st.selectbox(
        "Choose where you want to contribute:",
        ["Recycling", "Trees", "Money"]
    )

    amount = st.number_input("Enter donation amount (₹)", min_value=0)

    if st.button("Donate Now"):
        if amount > 0:
            st.success(f"🙏 Thank you for donating ₹{amount} towards {cause}!")
            st.balloons()
        else:
            st.warning("Please enter a valid amount.")
