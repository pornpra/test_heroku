from flask import Flask, request, jsonify
import predict_image as pi

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello BOTNOI !'

@app.route('/predict')
def predict():
    p_image_url = request.values['p_image_url']
    res = pi.predicting(p_image_url)

    if res == 0:
        return 'สิวของคุณอยู่ในระดับเล็กน้อย (Level 0) คำแนะนำ คือ ล้างหน้าอย่างสม่ำเสมอและพักผ่อนให้เพียงพอ'
    elif res == 1:
        return 'สิวของคุณอยู่ในระดับปานกลาง (Level 1) คำแนะนำ คือ ใช้ยาแต้มสิว'
    elif res == 2:
        return 'สิวของคุณอยู่ในระดับรุนแรง (Level 2) คำแนะนำ คือ ควรรีบมาพบแพทย์เฉพาะทาง ติดต่อจองคิวได้ที่ 02-999-9999'
    else:
        return 'ส่งรูปภาพสิวของคุณมาใหม่อีกครั้ง'

    result = {'result':res}
    #jsonify(result)

    return str(res)

if __name__ == '__main__':
    app.run(debug=True)
