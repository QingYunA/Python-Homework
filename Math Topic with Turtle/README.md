# Math Topic with Turtle

## 用法

```Python
python main.py
```

## 设计思路

1. 需要函数来生成随机数(2个)以及运算符
2. 需要函数确保生成的数与运算符满足条件(被整除，结果在[0, 99])
3. 海龟的正确运行
   - 在绘制试题与答案时，海龟goto到正确位置
   - 不同分辨率的屏幕的适配问题(采用相对距离来set海龟)
   - 带字方框的绘制，确保字体居中，方框位置合适

## 代码结构

`init_turtle()` : 初始化turtle，设置画布大小，画笔颜色，画笔粗细等
`sample()` : 从0-100中随机抽取两个数，并随机抽取运算符
`check` : 检验随机出的数与操作符是否满足条件(被整除，结果在[0, 99])
`turtle_go` : 绘制试题部分，控制turtle移动至指定位置
`turtle_go_answer` : 绘制答案部分，控制turtle移动至指定位置
`rect` : 绘制矩形
`rect_with_text` : 绘制带有文字的矩形(文字居中)

### 主函数main()

* 调用`init_turtle()`初始化turtle
* 进入5行3列的循环
* 调用`sample()`随机抽取两个数与运算符
* 调用`check()`检验抽取的数与运算符是否满足条件
* check()返回True, 调用turtle_go()绘制试题部分，调用turtle_go_answer()绘制答案部分，否则重新生成数与运算符

### 运行结果

![](https://cdn.jsdelivr.net/gh/QingYunA/my-img@main/20230320200952.png)
