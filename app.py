import numpy as np
import pandas as pd
import scipy
from scipy  import sparse
from sklearn.neighbors import NearestNeighbors
from werkzeug.utils import secure_filename
import re
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle
#app = FastAPI()


def load_files(file_name , ):
  with open (file_name, 'rb') as fp:
       res  = pickle.load(fp)
  return res

rating = pd.read_csv("rating.csv")
places = pd.read_csv("placeid.csv")
user_to_place_sparse = sparse.load_npz("sparcematrix.npz")
knn_model = NearestNeighbors(metric='cosine', algorithm='brute')
knn_model.fit(user_to_place_sparse)
user_to_place =  pd.read_csv("user_to_place.csv")
user_dict = load_files("user_dict")
place_dict = load_files("place_dict")
place_dictionary = load_files("place_dictionary")
place_list = load_files("place_list")


def predict_places(place:str,user:str,n_place:int,n_user:int):
    #n_user = 3
    #n_place = 5
    result = []
    def similar_places(place,n_place = 5):
      recommender = []
      ID = []
      place = [k for k, v in place_dictionary.items() if v == place][0]
      index = place_dict[place]
      knn_input = np.asarray([user_to_place.values[index]])
      n_place = min(len(place_list) - 1, n_place)
      distances, indices = knn_model.kneighbors(knn_input, n_neighbors=n_place + 1)
      for i in range(1, len(distances[0])):
           recommender.append(place_list[indices[0][i]])
           ID.append(place_dictionary[recommender[-1]])
      res = {"place_name": recommender, "place_id": ID}
      return res


    res =  similar_places(place,n_place)
    result.append(res)

    def similar_users(user,n_user):
        res = []
        users = []
        recommender = []
        ID = []
        user = user_dict[user]
        knn_input = np.asarray([user_to_place.values[user - 1]])
        distances, indices = knn_model.kneighbors(knn_input, n_neighbors=n_user + 1)

        for i in range(1, len(distances[0])):
            users.append(indices[0][i] + 1)
        for i in range(n_user):
            for place in (list(rating[(rating['user id'] == users[i]) & (rating["rate"] > 3)]['place name'])[:5]):
                if place not in result:
                    ID.append(place_dictionary[place])
                    recommender.append(place)
        res =  {"place_name": recommender, "place_id": ID}
        return res

    res  =  similar_users(user,n_user)
    result.append(res)
    return result

result =  predict_places("6249c7df30170c0174c4419a","62cb03b08ca3fa1264296dd7",5,2)
print(result)

"""""
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
"""""