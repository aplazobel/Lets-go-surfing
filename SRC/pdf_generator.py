import pandas as pd
from fpdf import FPDF

def pdfMaker():
    df = pd.read_csv("OUTPUT/beaches.csv")
    print(df.head())
    x = 0
    beach_name = df.iloc[x]["Name"]
    address = df.iloc[x]["Address"]
    direction = df.iloc[x]["Direction"]
    experience = df.iloc[x]["Experience"]
    bottom = df.iloc[x]["Bottom"]
    swell_height = df.iloc[x]["Swell Height"]
    swell_direction = df.iloc[x]["Swell direction"]
    wind_speed = df.iloc[x]["Wind speed"]
    wind_direction = df.iloc[x]["Wind direction"]
    water_temp = df.iloc[x]["Water temperature"]
    weather = df.iloc[x]["Weather Description"]

    pdf = FPDF()
    pdf.add_page()

    #Titulo de PDF
    pdf.image("INPUT/theboyz.JPG", x = 30, y = 10, w = 150, h = 100, type = '', link = '')

    #Nombre de Report y nombre de Playa
    pdf.set_xy(10,105)
    pdf.set_font("Courier", "", 24)
    pdf.cell(w=0, h = 20 , txt = f" Forecast report for {beach_name} ", border = 0, ln = 0, align = 'C', fill = False)

    # Subtitulo con el nivel recomendado del surfero
    pdf.set_xy(10,115)
    pdf.set_font("Courier", "B", 16)
    pdf.cell(w=0, h = 20 , txt = f" Recommended surfer experience: {experience} ", border = 0, ln = 0, align = 'C', fill = False)

    # Primera Fila de info con fotos
    pdf.set_xy(1,140)
    pdf.set_font("Courier", "", 14)
    if direction == "Right and left":
        pdf.cell(w=208, h = 20 , txt = f"    Direction: {direction}     Water Temp Cº: {water_temp}     Seabed: {bottom}    ", border = 0, ln = 0, align = 'C', fill = False)
    else:
        pdf.cell(w=208, h = 20 , txt = f" Direction: {direction}     Water Temp Cº: {water_temp}     Seabed: {bottom} ", border = 0, ln = 0, align = 'C', fill = False)
    # Para los iconos de la dirección de la ola 
    if direction == "Left":
        pdf.image("INPUT/left.png", x = 25, y = 160, w = 30, h = 30, type = '', link = '')
    elif direction == "Right":
        pdf.image("INPUT/right.png", x = 25, y = 160, w = 30, h = 30, type = '', link = '')
    elif direction == "Right and left":
        pdf.image("INPUT/right_and_left.png", x = 14, y = 160, w = 60, h = 30, type = '', link = '')
    else:
        pdf.image("INPUT/nan.png", x = 25, y = 160, w = 30, h = 30, type = '', link = '')

    # Para el icono del termometro de la temperatura del agua
    if water_temp < 15:
        pdf.image("INPUT/cold.jpg", x = 100, y = 160, w = 13, h = 25, type = '', link = '')
    elif 15 <= water_temp <= 22:
        pdf.image("INPUT/warm.png", x = 100, y = 160, w = 13, h = 25, type = '', link = '')
    elif water_temp > 22:
        pdf.image("INPUT/hot.png", x = 100, y = 160, w = 13, h = 25, type = '', link = '')

    # Para el suelo maritimo
    if bottom == "Reef-coral":
        pdf.image("INPUT/reef_coral.png", x = 160, y = 160, w = 20, h = 20, type = '', link = '')
    elif bottom == "Reef-rocky":
        pdf.image("INPUT/reef_rocky.png", x = 160, y = 160, w = 20, h = 20, type = '', link = '')
    elif bottom == "Beach-break" or bottom == "Sand-bar" or bottom == "Breakwater/jetty":
        pdf.image("INPUT/beach_break.png", x = 160, y = 160, w = 20, h = 20, type = '', link = '')
    elif bottom == "Point-break":
        pdf.image("INPUT/point_break.png", x = 160, y = 160, w = 20, h = 20, type = '', link = '')
    else:
        pdf.image("INPUT/nan.png", x = 25, y = 160, w = 30, h = 30, type = '', link = '')

    #Segunda Fila de info
    pdf.set_xy(1,190)
    pdf.set_font("Courier", "", 14)
    pdf.cell(w=208, h = 20 , txt = f" Weather: {weather}     Swell Height: {swell_height} ", border = 0, ln = 0, align = 'C', fill = False)

    # Para el tiempo
    if "cloud" in weather:
        pdf.image("INPUT/partly_cloudy.jpg", x = 60, y = 210, w = 30, h = 20, type = '', link = '')
    elif "sun" in weather:
        pdf.image("INPUT/sunny.jpg", x = 60, y = 210, w = 30, h = 20, type = '', link = '')
    elif "rain" in weather:
        pdf.image("INPUT/rainy.jpg", x = 60, y = 210, w = 30, h = 20, type = '', link = '')
    elif "storm" in weather:
        pdf.image("INPUT/storm.jpg", x = 60, y = 210, w = 30, h = 20, type = '', link = '')
    else:
        pdf.image("INPUT/nan.png", x = 60, y = 210, w = 30, h = 30, type = '', link = '')

    #Para el tamaño de las olas
    pdf.image("INPUT/swell.png", x = 130, y = 210, w = 30, h = 20, type = '', link = '')

    #Para info adicional
    pdf.set_xy(1,250)
    pdf.set_font("Courier", "B", 14)
    pdf.multi_cell(w=200, h = 10 , txt = f" ADDITIONAL INFO: Swell Direction = {swell_direction}, Wind Direction = {wind_direction}, Wind Speed = {wind_speed} kph ", border = 0,  align = 'C', fill = False)

    # Para la dirección de la playa 
    pdf.set_xy(0,275)
    pdf.set_font("Courier", "", 12)
    pdf.multi_cell(w=200, h = 10 , txt = f" Address: {address} ", border = 0,  align = 'C', fill = False)

    pdf.output("OUTPUT/forecastPDF.pdf")
