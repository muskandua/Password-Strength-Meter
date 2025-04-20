import streamlit as st
import re

# 🎉 Title
st.title("💡 Password Strength Meter By Dua Irfan Ahmed 🔐")

# 📝 Description
st.markdown("""
🚀 Welcome to the 🔐**Password Strength Meter Created By Dua Irfan Ahmed!** 🌟  
""")

# 🏷️ Input Field
password = st.text_input("🔑 Enter your password:", type="password")

# 🔍 Password Strength Check
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least **8 characters** long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include **both uppercase and lowercase** letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least **one number (0-9)**.")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least **one special character (!@#$%^&*)**.")

    return score, feedback


# ✅ Button to Check Password
if st.button("🔍 Check Password"):
    if password:
        score, feedback = check_password_strength(password)

    
        if score == 4:
            st.success("✅ Strong Password! Your password is secure.")
        elif score == 3:
            st.warning("⚠️ Moderate Password - Consider adding more security features.")
        else:
            st.error("❌ Weak Password - Improve it using the suggestions below.")

        if feedback:
            st.info("💡 Suggestions to improve your password:")
            for tip in feedback:
                st.write(tip)
    else:
        st.error("🚨 Please enter a password to check.")

# 🌟 Footer
st.markdown("""
----
Made with ❤️ by **Dua Irfan Ahmed** ❤️
""")
