import sys
from PyQt5.QtWidgets import QWidget,QLabel,QPushButton\
    ,QLineEdit,QTextEdit,QGridLayout,QApplication,QMainWindow\
    ,QVBoxLayout,QComboBox
from PyQt5.QtGui import QFont
from main.config import style

class Winform(QMainWindow):
    def __init__(self):
        super(Winform,self).__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle("故障申告")
        main_widge = QWidget()
        self.setCentralWidget(main_widge)
        title = QLabel("标题")
        author = QLabel("提交人")
        review = QLabel("申告内容")
        title.setStyleSheet("color:white")
        author.setStyleSheet("color:white")
        review.setStyleSheet("color:white")
        main_widge.setStyleSheet("background:#282a36")
        grid = QGridLayout()
        main_widge.setLayout(grid)
        self.setLayout(grid)
        grid.addWidget(title,0,2,1,2)
        grid.addWidget(author,1,3,1,2)
        grid.addWidget(review,1,4)
        left_widge = QWidget()
        grid.addWidget(left_widge, 0, 1, 4, 1)
        left_widge.setStyleSheet("background:#282a36")
        l_grid = QGridLayout()
        left_widge.setLayout(l_grid)
        left_widge_btn = QPushButton()
        left_widge_btn.setText("确定")
        l_grid.addWidget(left_widge_btn,9,0,1,8)
        left_widge_btn.setStyleSheet("border-width:1px;color:white;border-style:solid;border-color:#747474;background:#282a32;height:30px;width:40px")
        l_category_lable = QLabel("类别:")
        l_category_lable.setStyleSheet(style['label_style'])
        l_grid.addWidget(l_category_lable,0,1)
        l_category_combox = QComboBox()
        l_category_combox.addItem("现金")
        l_category_combox.addItem("优惠券")
        l_category_combox.addItem("视频vip")
        l_category_combox.setStyleSheet(style['combox_style'])
        l_grid.addWidget(l_category_combox,0,2,1,2)
        l_range_label = QLabel("金额:")
        l_range_label.setStyleSheet(style['label_style'])
        l_grid.addWidget(l_range_label,1,1)
        l_line_edit = QLineEdit()
        l_line_edit.setStyleSheet(style['l_line_edit'])
        l_line_edit.resize(30,70)
        l_line_edit.setPlaceholderText("红包最低金额")
        l_grid.addWidget(l_line_edit,1,2,1,2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Winform()
    win.resize(800,500)
    win.show()
    sys.exit(app.exec_())