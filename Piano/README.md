# Auto Play FreePiano

基于win32api，win32con，win32gui的FreePiano自动弹琴
部分思路来自于[e42s/FreePianoAutoPlayer](https://github.com/e42s/FreepianoAutoPlay)

## 1. 问题分析

### 1.1 任务拆解

使用键盘自动化工具，实现自动弹琴的主要任务点如下：
1. python打开FreePiano
2. python模拟键盘输入
3. 谱曲映射为键盘按键

### 1.2 键盘控制FreePiano

PyAutoGUI模拟的键盘事件无法直接传递到某些程序中，包括FreePiano。由于FreePiano使用了系统级别的钩子来捕获和处理键盘事件，而PyAutoGUI模拟的键盘事件只能被传递到Windows图形用户界面（GUI）层。

因此为了实现键盘自动化弹琴，我才用了win32api，win32con，win32gui这三个库来实现系统级别的键盘输入来控制FreePiano。

### 1.3 调节FreePiano的曲调

简谱拥有不同的曲调，如C大调，Db，Eb等，因此需要手动对FreePiano的曲调进行调节。

### 1.4 谱曲映射为键盘按键

如何将简谱映射为正确的键盘按键，是实现自动弹琴的关键。因为简谱中存在不同的音符，拍子速度，音符时长等因素，为了弹出正确的曲子，需要对按键的间隔严格限制。

### 2. 解决方案

### 2.1 打开FreePiano

这里采用 `subprocess` 库来打开FreePiano，因为FreePiano是一个exe文件，所以可以直接使用 `subprocess.Popen` 来打开。

```python {.line-numbers}}
subprocess. Popen(r'./freepiano/freepiano.exe')

```

### 2.2 模拟键盘输入

此处定义了一个类 `AutoPiano` 用于完整的实现所需的全部功能。

#### 2.2.1 注册hook及键盘事件

首先需要注册hook线程用于抓取系统级的键盘事件。

```python {.line-numbers}}
hook_thread = threading.Thread(target=self.hook)
hook_thread.start()
play_thread = threading.Thread(target=self.auto_play)
play_thread.start()
```

上述代码分别注册了两个线程，一个用于抓取系统级的键盘事件，一个用于模拟键盘输入。
hook函数的定义如下：
```python {.line-numbers}}

def hook(self):

    hook_manager = pyHook.HookManager()
    hook_manager.KeyDown = self.OnKeyboardEvent
    hook_manager.HookKeyboard()
    pythoncom.PumpMessages()
    pass

```
hook函数采用pyHook的HookManager来注册键盘事件，当键盘事件发生时，会调用 `OnKeyboardEvent` 函数来处理事件。OnKeyboardEvent函数定义如下：

```python {.line-numbers}}
def OnKeyboardEvent(self, event):
    if str(win32gui.GetWindowText(win32gui.GetForegroundWindow())).find("piano") is not -1:
        #control only when piano is not at foreground
        return True
    if chr(event.Ascii).isdigit():
        self.cur_song = int(chr(event.Asciiqq))
    elif chr(event.Ascii) == 's':
        self.state = 'pause'
    elif chr(event.Ascii) == 'p':
        self.state = 'play'
    elif chr(event.Ascii) == 'q':
        self.state = 'stop'
        exit(0)
    # return True to pass the event to other handlers
    return 
```

OnKeyboardEvent用于改变类中的成员变量的状态，用于在弹奏过程中使用。

#### 2.2.2 调用win32api实现键盘按下

此处采用win32api来实现键盘按下，核心代码为

```python {.line-numbers}}

hwsc = win32api. MapVirtualKey(VK_CODE[line[0]], 0)
win32api.keybd_event(VK_CODE[line[0]], hwsc, 0, 0)

```
此处需要先预设好VK_CODE字典，用于将按键映射为win32api中的键盘码，然后调用win32api的keybd_event函数来实现键盘按下。

完整代码见main.py函数

### 2.3 调节FreePiano的曲调

此处使用pyautogui来实现键盘移动，并多次点击，调节到正确的曲调。

```python {.line-numbers}}
pyautogui.click(770, 630, clicks=2, interval=0.2, duration=0.6) #* 调节为D大调
```

### 2.4 谱曲映射为键盘按键

根据[十分钟看懂简谱](https://www.sohu.com/a/420248125_658910)中的方法，我手动将简谱转换为了数字，示例如下：

```python {.line-numbers}}
1 800 0
1 600 0
2 200 0
2 400 0
1 800 0
y 200 0
1 200 0
```
其中，每一行代表一个音符，具体释义如下：
第一个数字代表实际按下的键盘按键
第二个数字代表按下的时间，单位为ms
第三个数字代表间隔时长，单位为ms。

### 结果展示

见文件夹下的七里香.mp4录屏
