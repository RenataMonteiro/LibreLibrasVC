#!flask/bin/python
from flask import Flask, request, Response
import time
import cv2
import sys
from flask import Flask, request, Response, jsonify
from wekapy import Model, Instance, Feature
from tsfresh import extract_features

PATH_TO_TEST_IMAGES_DIR = './images'

app = Flask(__name__)


@app.route('/')
def index():
    return Response(open('./teste.html').read(), mimetype="text/html")

# save the image as a picture

def create_instance(file):
    	features = extract_features(file)
	instance = Instance()
	instance.add_features([
		Feature(name="feat1", value=features[0], possible_values="numeric"),
		Feature(name="feat2", value=features[1], possible_values="numeric"),
		Feature(name="feat3", value=features[2], possible_values="numeric"),
		Feature(name="feat4", value=features[3], possible_values="numeric"),
		Feature(name="feat5", value=features[4], possible_values="numeric"),
		Feature(name="feat6", value=features[5], possible_values="numeric"),
		Feature(name="feat7", value=features[6], possible_values="numeric"),
		Feature(name="class", value="?", possible_values="{A, B, C, D, E}")])
	return instance


@app.route('/image', methods=['POST'])
def image():

    i = request.files['image']  # get the image
    f = ('%s.jpeg' % time.strftime("%Y%m%d-%H%M%S"))
    i.save('%s/%s' % (PATH_TO_TEST_IMAGES_DIR, f))

    model = Model(classifier_type = "trees.RandomForest", classpath = "weka.jar")
    model.load_model("random_forest.model")
    model.add_test_instance(create_instance("images/imgem.jpeg"))
    model.test()
    print(model.predictions)
    predictions = model.predictions
    resultado = {'descricao': predictions[0]}
    return jsonify({'resultado': resultado})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
