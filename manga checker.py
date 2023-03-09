import PySimpleGUI as sg
import main
import webbrowser

list = []
users = main.get_list()
date = 'Last checked ' + main.get_date()
last = []

#define layout
layout1 = [ [sg.Text('Name', background_color='Black', font = ('Yu Gothic UI Semilight', 15) ), sg.Input('',k='-FILTER-', focus=True, font=('Yu Gothic UI Semilight', 15),)], 
            [sg.Button('  Search  ', font = ('Yu Gothic UI Semilight', 12)), sg.Button('    Add    ', font = ('Yu Gothic UI Semilight', 12))],
            [sg.Table(headings =['Manga Name'], values = list, k='-TABLE-',num_rows=20, font = ('Yu Gothic UI Semilight', 12), hide_vertical_scroll=True, auto_size_columns=False, def_col_width=(85), justification='left', enable_events=True, row_height=30, background_color='Black')]
         ]

layout2=[[sg.Button('  Remove  ', font = ('Yu Gothic UI Semilight', 12))],
         [sg.Table(headings =['Manga Name'], values = users, k='-TABLE2-',num_rows=20, font = ('Yu Gothic UI Semilight', 12), auto_size_columns=False, def_col_width=(85), justification='left', enable_events=True, row_height=30, background_color='Black')]
         ]

layout3= [[sg.Button('   Remind   ', font = ('Yu Gothic UI Semilight', 12)), sg.Button('  Open URL  ', font = ('Yu Gothic UI Semilight', 12))],
          [sg.Text(date, k='-DATE-', background_color='Black', text_color='White', font = ('Yu Gothic UI Semilight', 15))],
          [sg.Table(headings =['            Manga Name            ', '  Newest Chapter  ', '   Uploaded   '], values = list, font = ('Yu Gothic UI Semilight', 10),k='-TABLE3-',num_rows=20, auto_size_columns=True, justification='left', enable_events=True, row_height=30, background_color='Black')]
         ]

#Define Layout with Tabs         
tabgrp = [[sg.TabGroup([[sg.Tab('                         Search                          ', layout1, title_color='Red', k = 'tab1', border_width =10, background_color='Black'),
                    sg.Tab('                         My List                          ', layout2,title_color='Blue',background_color='Black'),
                    sg.Tab('                         Remind                         ', layout3,title_color='Black',background_color='Black')]], tab_location='topleft',
                       title_color='Black', tab_background_color='Gray',selected_title_color='Red',
                       selected_background_color='Gray', border_width=0, size=(770, 760), background_color='Black', font = ('Yu Gothic UI Semilight', 12))]]  
        
#Define Window
window =sg.Window("Manga Reminder",tabgrp, size=(800, 800), icon=r'data\makima hotdog.ico', background_color='Black')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '  Search  ':
      tmp = main.search(values['-FILTER-'])
      list = tmp
      window.Element('-TABLE-').update(tmp)
    elif event == '    Add    ' and len(values['-TABLE-']) > 0:
      index = values['-TABLE-'][0]
      main.add_to_list(list[index][0])
      users = main.get_list()
      window.Element('-TABLE2-').update(users)
    elif event == '   Remind   ':
      t = main.check_new()
      last = t
      date = 'Last checked ' + main.get_date()
      window.Element('-DATE-').update(date)
      window.Element('-TABLE3-').update(t)
    elif event == '  Open URL  'and len(values['-TABLE3-']) > 0:
      index = values['-TABLE3-'][0]
      browser = webbrowser.get()
      browser.open_new(t[index][3])
    elif event == '  Remove  'and len(values['-TABLE2-']) > 0:
      indexes = values['-TABLE2-']
      rem = []
      for i in indexes:
         rem.append(users[i][0])
      #print(rem)
      for j in rem:
         main.remove_from_list(j)
      users = main.get_list()
      window.Element('-TABLE2-').update(users)
      


#access all the values and if selected add them to a string
window.close()    