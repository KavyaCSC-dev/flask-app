from flask import Flask, render_template, request, send_file
from fpdf import FPDF

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():

    application = request.form['application']
    qua = request.form['qualification']
    req1 = request.form['req1']
    req2 = request.form['req2']
    req3 = request.form['req3']
    req4 = request.form['req4']
    req5 = request.form['req5']
    req6 = request.form['req6']
    req7 = request.form['req7']
    req8 = request.form['req8']
    last_date = request.form['last_date']
    contact_no = request.form['contact_no']
    online_fee = request.form['online_fee']
    sc_fees = request.form['sc_fees']

    # Create a new PDF object
    pdf = FPDF()
    pdf.add_page()

    # Set font and font size
    pdf.set_font("Arial", size=14)

    # Add content to the PDF
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", size=19 ,style="BU")
    pdf.cell(200, 10, txt="Kavya CSC Center", ln=1, align="C")
    pdf.set_text_color(255, 0, 0)
    pdf.set_font("Arial", size=48)
    pdf.cell(200, 20, txt="Job Notification..!", ln=1, align="C")
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", style="BU", size=20)
    pdf.cell(200, 18, txt=application, ln=1, align="C")
    pdf.set_font("Arial", style="BU", size=20)
    pdf.cell(200, 10, txt="1. Required Qualification: " + qua, ln=1)
    pdf.cell(200, 10, txt="2. Required Documents:", ln=1)
    pdf.set_font("Arial", style="" ,size=18)
    pdf.cell(200, 10, txt="--"+req1, ln=1)
    pdf.cell(200, 10, txt="--"+req2, ln=1)
    pdf.cell(200, 10, txt="--"+req3, ln=1)
    pdf.cell(200, 10, txt="--"+req4, ln=1)
    pdf.cell(200, 10, txt="--"+req5, ln=1)
    pdf.cell(200, 10, txt=req6, ln=1)
    pdf.cell(200, 10, txt=req7, ln=1)
    pdf.cell(200, 10, txt=req8, ln=1)
    pdf.set_text_color(250,0,0)
    pdf.set_font("Arial", style="BU")
    pdf.cell(200, 10, txt="Note:", ln=1)
    pdf.set_text_color(0,0,0)
    pdf.set_font("Arial", style="", size=15)
    pdf.cell(200, 10, txt="Last Date ON: " + last_date, ln=1)
    pdf.set_font("Arial", style="")
    pdf.cell(200, 10, txt="Contact US For More Information: " + contact_no, ln=2)

    pdf.set_y(250)
    pdf.set_font("Arial", style="I", size=12)
    pdf.cell(200, 10, txt="Online Fees For OBC/General: " + online_fee, ln=1)
    pdf.cell(200, 10, txt="Online Fees For SC/ST: " + sc_fees, ln=1)



    pdf_path = "job_notification.pdf"
    pdf.output(pdf_path)

    return send_file(pdf_path, as_attachment=True)
if __name__ == '__main__':
    app.run(debug=True)



