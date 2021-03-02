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
        output = 'สิวของคุณอยู่ในระดับเล็กน้อย (Level 0) คำแนะนำ คือ ล้างหน้าอย่างสม่ำเสมอและพักผ่อนให้เพียงพอ'
        #return output
    elif res == 1:
        output = 'สิวของคุณอยู่ในระดับปานกลาง (Level 1) คำแนะนำ คือ ใช้ยาแต้มสิว'
        #return output
    elif res == 2:
        output = 'สิวของคุณอยู่ในระดับรุนแรง (Level 2) คำแนะนำ คือ ควรรีบมาพบแพทย์เฉพาะทาง ติดต่อจองคิวได้ที่ 02-xxx-xxxx'
        #return output
    else:
        output = 'ส่งรูปภาพสิวของคุณมาใหม่อีกครั้ง'
        #return output

    result = {'result':output}
    #jsonify(result)

    return jsonify(result)
    #str(res)

if __name__ == '__main__':
    app.run(debug=True)
