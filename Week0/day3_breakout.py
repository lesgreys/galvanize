from math import sqrt

def confidence_interval(p,n,std):
    ME = round((sqrt(p*(1-p)/n)),2)*std

    lower = round(p - ME,2)
    upper = round(p + ME,2)


    return ME, lower, upper