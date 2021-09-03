import re
import time
import pywinauto

import tdx

_exe_name = r'D:\new_zheshang\TdxW.exe'
_win_login = '浙商证券通达信V.*'
_win_dlg = '^浙商证券$'
_win_main = '浙商证券通达信V.* \-'

def lonin(app):
    app.top_window().child_window(control_id=0x16d, class_name='AfxWnd100').click_input()
    #app.top_window().child_window(control_id=1, class_name='AfxWnd100').click_input()
    
def layout(app):
    app.top_window().type_keys('^m', set_foreground=True)
    app.window(title_re='.*多股同列').wait('enabled', timeout=30)
    wnd = app.top_window().child_window(title='分析图表-多股同列')
    wnd = wnd.child_window(control_id=0xd5, class_name='CFQS_SwitchEx')
    wnd.click_input(coords=(80, 10))
    app.top_window().maximize()
    time.sleep(10)
    app.top_window().type_keys('{VK_UP}{VK_UP}{VK_UP}', set_foreground=True)
    
def run():
    #app = tdx.connect(_exe_name)
    app = tdx.start(_exe_name)
    result = app.window(title_re=_win_login).wait('enabled', timeout=30)
    if result:
        lonin(app)

    result = app.window(title_re=f'({_win_dlg})|({_win_main})').wait('enabled', timeout=30)
    if result:
        if re.search(_win_dlg, app.top_window().window_text()):
            tdx.dlg_close(app)
    
        result = app.window(title_re=_win_main).wait('enabled', timeout=30)
        if result:
            layout(app)
            
    print('Ok.')

def run_quit():
    app = tdx.kill(_exe_name)
    
if __name__ == '__main__':
    run()
