from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from gensim.summarization import keywords, summarize
from gensim.models import Doc2Vec

from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model
from keras import backend as K
import numpy as np
import json

from sklearn.cluster import KMeans

@csrf_exempt
def get_features(request):
	data = {"success": False}
	
	if request.method == "POST":
		text = request.POST['data']
		d2v = Doc2Vec.load('trained_models/doc2vec.bin')
		embedding = d2v.infer_vector(text)

		embedding = np.reshape(embedding, (1,-1))
		
		model = Sequential()
		model.add(Dense(90, input_dim=300, activation='sigmoid'))
		model.add(Dense(10, activation='sigmoid'))
		model.add(Dense(90, activation='sigmoid'))
		model.add(Dense(300, activation='sigmoid'))
		model.compile(optimizer='adam', loss='mse')

		K.clear_session()
		model = load_model('trained_models/autoencoder.bin')
		get_int_layer_pred = K.function([model.layers[0].input], [model.layers[1].output])
		pred = get_int_layer_pred([embedding])[0]

		model.fit(embedding, embedding, epochs=10)
		model.save('trained_models/autoencoder.bin')

		data['success'] = True
		data['pred'] = str(pred[0])

	return JsonResponse(data)


@csrf_exempt
def get_clusters(request):
	data = {"success": False}
	
	if request.method == "POST":

		allvec = []
		veclabels = []

		vec_data = json.loads(request.POST['data'])
		for vd in vec_data:
			# veclabels.append(vd['href'][12:min(25, len(vd['href'])-1)])
			veclabels.append(vd['href'])
			allvec.append([float(x) for x in vd['vec'].replace('\n', ' ').strip()[1:-1].split()])

		allvec = np.array(allvec)

		clust = KMeans(n_clusters=3)
		clust.fit(allvec)

		data['success'] = True
		data['labels'] = clust.labels_

	return JsonResponse(data)
	