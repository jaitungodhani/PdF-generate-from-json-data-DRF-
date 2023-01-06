# import requests
# import json

# url = "http://127.0.0.1:8000/api/invoices/"

# payload = json.dumps({
#   "cash_in_bank": -14.61,
#   "total_current_assets": -14.61,
#   "total_assets": -14.61,
#   "net_income": 0,
#   "opening_balance_equity": -23.45,
#   "owner_loan": 576,
#   "retained_earnings": -567.16
# })
# headers = {
#   'Content-Type': 'application/json'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Flowable, FrameBreak, KeepTogether, PageBreak, Spacer
from reportlab.platypus import Frame, PageTemplate, KeepInFrame
from reportlab.lib.units import cm
from reportlab.platypus import (Table, TableStyle, BaseDocTemplate)

styleSheet = getSampleStyleSheet()

########################################################################

def create_pdf():
    """
    Create a pdf
    """

    # Create a frame
    text_frame = Frame(
        x1=3.00 * cm,  # From left
        y1=1.5 * cm,  # From bottom
        height=19.60 * cm,
        width=15.90 * cm,
        leftPadding=0 * cm,
        bottomPadding=0 * cm,
        rightPadding=0 * cm,
        topPadding=0 * cm,
        showBoundary=1,
        id='text_frame')

    # Create text

    L = [Paragraph("""What concepts does PLATYPUS deal with?""", styleSheet['Heading2']),
                          Paragraph("""
                         The central concepts in PLATYPUS are Flowable Objects, Frames, Flow
                         Management, Styles and Style Sheets, Paragraphs and Tables.  This is
                         best explained in contrast to PDFgen, the layer underneath PLATYPUS.
                         PDFgen is a graphics library, and has primitive commans to draw lines
                         and strings.  There is nothing in it to manage the flow of text down
                         the page.  PLATYPUS works at the conceptual level fo a desktop publishing
                         package; you can write programs which deal intelligently with graphic
                         objects and fit them onto the page.
                         """, styleSheet['BodyText']),

                          Paragraph("""
                         How is this document organized?
                         """, styleSheet['Heading2']),

                          Paragraph("""
                         Since this is a test script, we'll just note how it is organized.
                         the top of each page contains commentary.  The bottom half contains
                         example drawings and graphic elements to whicht he commentary will
                         relate.  Down below, you can see the outline of a text frame, and
                         various bits and pieces within it.  We'll explain how they work
                         on the next page.
                         """, styleSheet['BodyText']),
                          ]






    # Building the story
    story = L * 50 # (alternative, story.add(L))
    story.append(KeepTogether([]))

    # Establish a document
    doc = BaseDocTemplate("Example_output.pdf", pagesize=letter)

    # Creating a page template
    frontpage = PageTemplate(id='FrontPage',
                             frames=[text_frame]
                             )
    # Adding the story to the template and template to the document
    doc.addPageTemplates(frontpage)

    # Building doc
    doc.build(story)


# ----------------------------------------------------------------------
if __name__ == "__main__":
    create_pdf() # Printing the pdf 

tdata = [["name", "fname"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"], ["jaitun","Godhani"]]
tdata.append(["Jaitun", Paragraph("As we all know, a paragraph is a group of sentences that are connected and makes absolute sense. While writing a long essay or letter, we break them into paragraphs for better understanding, and to make a well-structured writing piece. Paragraph writing on any topic is not only about expressing your thoughts on the given topic, but it is also about framing ideas about the topic and making it convenient for the readers to follow it. In English paragraph writing, it is essential to focus on the writing style, i.e., the flow and connection between the sentences.Therefore, a paragraph must be written in simple language in order to avoid any interruption while reading. In order to write a paragraph on any topic, you can refer to the samples given below, and write a paragraph without any hindrance. \
                As we all know, a paragraph is a group of sentences that are connected and makes absolute sense. While writing a long essay or letter, we break them into paragraphs for better understanding, and to make a well-structured writing piece. Paragraph writing on any topic is not only about expressing your thoughts on the given topic, but it is also about framing ideas about the topic and making it convenient for the readers to follow it. In English paragraph writing, it is essential to focus on the writing style, i.e., the flow and connection between the sentences.Therefore, a paragraph must be written in simple language in order to avoid any interruption while reading. In order to write a paragraph on any topic, you can refer to the samples given below, and write a paragraph without any hindrance. \
                    As we all know, a paragraph is a group of sentences that are connected and makes absolute sense. While writing a long essay or letter, we break them into paragraphs for better understanding, and to make a well-structured writing piece. Paragraph writing on any topic is not only about expressing your thoughts on the given topic, but it is also about framing ideas about the topic and making it convenient for the readers to follow it. In English paragraph writing, it is essential to focus on the writing style, i.e., the flow and connection between the sentences.Therefore, a paragraph must be written in simple language in order to avoid any interruption while reading. In order to write a paragraph on any topic, you can refer to the samples given below, and write a paragraph without any hindrance. \
                        As we all know, a paragraph is a group of sentences that are connected and makes absolute sense. While writing a long essay or letter, we break them into paragraphs for better understanding, and to make a well-structured writing piece. Paragraph writing on any topic is not only about expressing your thoughts on the given topic, but it is also about framing ideas about the topic and making it convenient for the readers to follow it. In English paragraph writing, it is essential to focus on the writing style, i.e., the flow and connection between the sentences.Therefore, a paragraph must be written in simple language in order to avoid any interruption while reading. In order to write a paragraph on any topic, you can refer to the samples given below, and write a paragraph without any hindrance. \
                            As we all know, a paragraph is a group of sentences that are connected and makes absolute sense. While writing a long essay or letter, we break them into paragraphs for better understanding, and to make a well-structured writing piece. Paragraph writing on any topic is not only about expressing your thoughts on the given topic, but it is also about framing ideas about the topic and making it convenient for the readers to follow it. In English paragraph writing, it is essential to focus on the writing style, i.e., the flow and connection between the sentences.Therefore, a paragraph must be written in simple language in order to avoid any interruption while reading. In order to write a paragraph on any topic, you can refer to the samples given below, and write a paragraph without any hindrance.")])
