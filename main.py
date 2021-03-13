import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.ui import Ui_Form
import selflib.azrmath as azrmath

class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.leftXP_calc_buttom.clicked.connect(self.xpleft)
        self.diff_ratio_calc_button01.clicked.connect(self.chapter_diff)
        self.diff_ratio_calc_button02.clicked.connect(self.chapter_diff_B)
        self.XPgain_calc_button01.clicked.connect(self.XPgain_A)
        self.XPgain_calc_button02.clicked.connect(self.XPgain_B)
        self.oilcost_calc_button.clicked.connect(self.oilcost)

    def xpleft(self):
        current_lv = self.currentLV_input.text()
        target_lv = self.targetLV_input.text()
        current_xp = self.currentXP_intput01.text()
        input_checked = 1
        data_list = [current_lv, target_lv, current_xp]
        for i in data_list:
            for j in i:
                if ord(j) > 57 or ord(j) < 48:
                    input_checked = 0
        try:
            current_lv = int(data_list[0])
            target_lv = int(data_list[1])
            current_xp = int(data_list[2])

            if current_lv > 120 or current_lv < 1: input_checked = 0
            if target_lv > 120 or target_lv < 1: input_checked = 0
            if target_lv < current_lv: input_checked = 0
            if current_xp < 0: input_checked = 0
            if input_checked == 0:
                self.leftxp_output.setText('Error')
            else:
                if self.isnormal_checkbox.isChecked():
                    result = azrmath.ship_xp(target_lv, False) - azrmath.ship_xp(current_lv, False) - current_xp
                    self.leftxp_output.setText(str(result) + ' ' + 'EXP')
                else:
                    result = azrmath.ship_xp(target_lv, True) - azrmath.ship_xp(current_lv, True) - current_xp
                    self.leftxp_output.setText(str(result) + ' ' + 'EXP')
        except:
            if input_checked == 0:
                self.leftxp_output.setText('Error')

    def chapter_diff(self):
        chapter = self.chapter_input_a.text()
        section = self.section_input.text()
        aver_level = self.aver_level_input.text()
        antiair = self.antiair_input.text()
        air_ctrl = self.airctrl_input.text()
        front_num = self.frontsize_input.text()
        back_num = self.backsize_input.text()

        input_checked = 1
        data_list = [chapter, section, aver_level, antiair, air_ctrl, front_num, back_num]
        for i in data_list:
            for j in i:
                if ord(j) > 57 or ord(j) < 48:
                    input_checked = 0
        try:
            chapter = int(data_list[0])
            section = int(data_list[1])
            aver_level = int(data_list[2])
            antiair = int(data_list[3])
            air_ctrl = int(data_list[4])
            front_num = int(data_list[5])
            back_num = int(data_list[6])

            if chapter > 18 or chapter < 1:
                input_checked = 0
            elif 1 <= chapter <= 13:
                if section > 4 or section < 1:
                    input_checked = 0
            elif 14 <= chapter <= 17:
                if section > 3 or section < 1:
                    input_checked = 0
            elif chapter == 18:
                if section != 1:
                    input_checked = 0

            if aver_level > 120 or aver_level < 1: input_checked = 0
            if antiair < 0: input_checked = 0
            if air_ctrl < 0: input_checked = 0
            if front_num > 3 or front_num < 1: input_checked = 0
            if back_num > 3 or back_num < 1: input_checked = 0
            if input_checked == 0:
                self.difficulty_ratio_output.setText('Error')
            else:
                difficulty_ratio = azrmath.chapter_diffculty(chapter, section, aver_level, antiair, air_ctrl, front_num,
                                                             back_num)
                self.difficulty_ratio_output.setText(str(difficulty_ratio))
        except:
            if input_checked == 0:
                self.difficulty_ratio_output.setText('Error')

    def chapter_diff_B(self):
        chapter = self.chapter_input_a_2.text()
        section = self.section_input_2.text()
        aver_level = self.aver_level_input_2.text()
        antiair = self.antiair_input_2.text()
        air_ctrl = self.airctrl_input_2.text()
        front_num = self.frontsize_input_2.text()
        back_num = self.backsize_input_2.text()

        input_checked = 1
        data_list = [chapter, section, aver_level, antiair, air_ctrl, front_num, back_num]
        for i in data_list:
            for j in i:
                if ord(j) > 57 or ord(j) < 48:
                    input_checked = 0
        try:
            chapter = int(data_list[0])
            section = int(data_list[1])
            aver_level = int(data_list[2])
            antiair = int(data_list[3])
            air_ctrl = int(data_list[4])
            front_num = int(data_list[5])
            back_num = int(data_list[6])

            if chapter > 18 or chapter < 1:
                input_checked = 0
            elif 1 <= chapter <= 13:
                if section > 4 or section < 1:
                    input_checked = 0
            elif 14 <= chapter <= 17:
                if section > 3 or section < 1:
                    input_checked = 0
            elif chapter == 18:
                if section != 1:
                    input_checked = 0

            if aver_level > 120 or aver_level < 1: input_checked = 0
            if antiair < 0: input_checked = 0
            if air_ctrl < 0: input_checked = 0
            if front_num > 3 or front_num < 1: input_checked = 0
            if back_num > 3 or back_num < 1: input_checked = 0
            if input_checked == 0:
                self.difficulty_ratio_output_2.setText('Error')
            else:
                difficulty_ratio = azrmath.chapter_diffculty(chapter, section, aver_level, antiair, air_ctrl, front_num,
                                                             back_num)
                self.difficulty_ratio_output_2.setText(str(difficulty_ratio))
        except:
            if input_checked == 0:
                self.difficulty_ratio_output_2.setText('Error')

    def XPgain_A(self):
        chapter = self.chapter_input_a_3.text()
        section = self.section_input_3.text()
        input_checked = 1
        data_list = [chapter, section]
        for i in data_list:
            for j in i:
                if ord(j) > 57 or ord(j) < 48:
                    input_checked = 0
        try:
            chapter = int(data_list[0])
            section = int(data_list[1])

            if chapter > 18 or chapter < 1:
                input_checked = 0
            elif 1 <= chapter <= 13:
                if section > 4 or section < 1:
                    input_checked = 0
            elif 14 <= chapter <= 17:
                if section > 3 or section < 1:
                    input_checked = 0
            elif chapter == 18:
                if section != 1:
                    input_checked = 0
            if input_checked == 0:
                self.xpgain_output_01.setText('Error')
            else:
                total_xp, xp_per_access = azrmath.chapter_xp(chapter, section)
                self.xpgain_output_01.setText('T:' + str(total_xp) + 'EXP\n' + 'S:' + str(xp_per_access) + 'EXP')
        except:
            if input_checked == 0:
                self.xpgain_output_01.setText('Error')

    def XPgain_B(self):
        chapter = self.chapter_input_a_4.text()
        section = self.section_input_4.text()
        input_checked = 1
        data_list = [chapter, section]
        for i in data_list:
            for j in i:
                if ord(j) > 57 or ord(j) < 48:
                    input_checked = 0
        try:
            chapter = int(data_list[0])
            section = int(data_list[1])

            if chapter > 18 or chapter < 1:
                input_checked = 0
            elif 1 <= chapter <= 13:
                if section > 4 or section < 1:
                    input_checked = 0
            elif 14 <= chapter <= 17:
                if section > 3 or section < 1:
                    input_checked = 0
            elif chapter == 18:
                if section != 1:
                    input_checked = 0
            if input_checked == 0:
                self.xpgain_output_02.setText('Error')
            else:
                total_xp, xp_per_access = azrmath.chapter_xp(chapter, section)
                self.xpgain_output_02.setText('T:' + str(total_xp) + 'EXP\n' + 'S:' + str(xp_per_access) + 'EXP')
        except:
            if input_checked == 0:
                self.xpgain_output_02.setText('Error')

    def oilcost(self):
        current_lv = self.currentLV_input_2.text()
        target_lv = self.targetLV_input_2.text()
        single_oil = self.currentLV_input_3.text()
        chapter = self.chapter_input_a_5.text()
        section = self.section_input_5.text()
        current_xp = self.currentXP_intput02.text()

        data_list = [chapter, section, current_lv, target_lv, single_oil, current_xp]
        input_checked = 1
        for i in data_list:
            for j in i:
                if ord(j) > 57 or ord(j) < 48:
                    input_checked = 0
        try:
            chapter = int(data_list[0])
            section = int(data_list[1])
            current_lv = int(data_list[2])
            target_lv = int(data_list[3])
            single_oil = int(data_list[4])
            current_xp = int(data_list[5])

            if chapter > 18 or chapter < 1:
                input_checked = 0
            elif 1 <= chapter <= 13:
                if section > 4 or section < 1:
                    input_checked = 0
            elif 14 <= chapter <= 17:
                if section > 3 or section < 1:
                    input_checked = 0
            elif chapter == 18:
                if section != 1:
                    input_checked = 0
            if current_lv > 120 or current_lv < 1: input_checked = 0
            if target_lv > 120 or target_lv < 1: input_checked = 0
            if target_lv < current_lv: input_checked = 0
            if current_xp < 0: input_checked = 0
            if input_checked == 0:
                self.leftxp_output_4.setText('Error')
            else:
                if self.isnormal_checkbox_2.isChecked():
                    leftxp = azrmath.ship_xp(target_lv, False) - azrmath.ship_xp(current_lv, False) - current_xp
                else:
                    leftxp = azrmath.ship_xp(target_lv, True) - azrmath.ship_xp(current_lv, True) - current_xp

                totol_xp, xp_per_acess = azrmath.chapter_xp(chapter, section)
                total_oilcost = int((leftxp / xp_per_acess) * single_oil + 0.5)
                self.leftxp_output_4.setText(str(total_oilcost))
        except:
            if input_checked == 0:
                self.leftxp_output_4.setText('Error')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
