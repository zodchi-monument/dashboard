#from sklearn.covariance import EllipticEnvelope
import plotly.graph_objects as go
import numpy as np

def cut_dev(data, cn=0.005, verbose=True):
    """
    Метод для детекции и очистки аномалий
    data: Series or 1d np.array - данные
    cn: int - contamination, регулирует степень очистки
    verbose: bool - вкл/выкл визуализация д
    return: np.array - выбросы помечены как None
    """
    #d = np.array(data)
    #mask = d.reshape(-1, 1)
    #model = EllipticEnvelope(contamination=cn).fit(mask)
    #mask = (model.predict(mask)+1).astype(bool)
    #d[~mask] = None
    #if verbose:
    #    fig = go.Figure()
    #    fig.add_trace(go.Scatter(y = data,mode='lines',name='raw',
    #                     line = dict(color='royalblue', width=1, dash='dash')))
    #    fig.add_trace(go.Scatter(y = d,mode='lines',name='enveloped'))
    #    fig.show()
    #return d
    pass

def MAPE(t, p):
    t, p = np.array(t),np.array(p)
    t, p = np.squeeze([t,p])
    mask = t != 0
    err = (np.fabs(t - p)/t)[mask].mean()*100
    return round(err,3)