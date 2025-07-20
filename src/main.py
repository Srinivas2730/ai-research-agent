import streamlit as st
from dotenv import load_dotenv
import os
from agent_nodes import planner_node, searcher_node, summarizer_node
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

load_dotenv()

def generate_pdf(plan, summary):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 50, "📝 Research Plan:")
    c.setFont("Helvetica", 12)
    y = height - 70
    for line in plan.split('\n'):
        c.drawString(50, y, line)
        y -= 15
        if y < 50:
            c.showPage()
            y = height - 50

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y - 20, "📄 Summary:")
    c.setFont("Helvetica", 12)
    y -= 40
    for line in summary.split('\n'):
        c.drawString(50, y, line)
        y -= 15
        if y < 50:
            c.showPage()
            y = height - 50

    c.save()
    buffer.seek(0)
    return buffer

def main():
    st.title("🧠 Research Assistant with Groq")

    topic = st.text_input("Enter your research topic:")

    if topic and st.button("Run Research Pipeline"):
        with st.spinner("Planning..."):
            plan = planner_node(topic)
            st.subheader("📝 Plan")
            st.write(plan)

        with st.spinner("Searching..."):
            search_results = searcher_node(topic)
            st.subheader("🔍 Search Results")
            st.write(search_results)

        search_text = "\n".join(search_results) if isinstance(search_results, list) else str(search_results)

        with st.spinner("Summarizing..."):
            summary, confidence = summarizer_node(search_text)
            st.subheader("📄 Summary")
            st.write(summary)
            st.metric("🔒 Confidence Score", f"{int(confidence * 100)}%")

        pdf_buffer = generate_pdf(plan, summary)
        st.download_button(
            label="📥 Download Plan + Summary as PDF",
            data=pdf_buffer,
            file_name="research_output.pdf",
            mime="application/pdf"
        )

if __name__ == "__main__":
    main()




