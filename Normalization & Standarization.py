#Normalization
from sklearn.preprocessing import MinMaxScaler
data = [[12000000, 33], [35000000, 45], [4000000, 23], [6500000, 26], [9000000, 29]]

scaler = MinMaxScaler()
scaler.fit(data)

print(scaler.transform(data))

#Standarization
from sklearn import preprocessing

data = [[12000000, 33], [35000000, 45], [4000000, 23], [6500000, 26], [9000000, 29]]
scaler = preprocessing.StandardScaler().fit(data)
data = scaler.transform(data)
print(data)