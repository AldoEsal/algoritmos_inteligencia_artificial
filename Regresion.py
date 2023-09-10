from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split

boston = datasets.load_boston()
print(boston)
print()

print("Informacion en el dataset: ")
print(boston.keys())
print()

print("Caracteristicas por columna del dataset: ")
print(boston.DESCR)

print("Cantidad de casas: ")
print(boston.data.shape[0])
print()
print("Cantidad de variables: ")
print(boston.data.shape[1])
print()

print("Nombres de variables/columnas a tomar en cuenta: ")
print(boston.feature_names)
print()

X_multiple = boston.data[:,5:8]
print(X_multiple)
print()

y_multiple=boston.target


X_train, X_test, y_train, y_test=train_test_split(X_multiple,y_multiple,test_size=0.2)

lr_multiple = linear_model.LinearRegression()

lr_multiple.fit(X_train,y_train)

Y_pred_multiple=lr_multiple.predict(X_test)


print("DATOS DEL MODELO GENERADO:")
print()
print("Valores de las pendientes: ")
print(lr_multiple.coef_)
print()
print("Valores de la interseccion o coeficiente: ")
print(lr_multiple.intercept_)
print()
print("Valores de la interseccion o coeficiente: ")
print(lr_multiple.score(X_train,y_train))
print()