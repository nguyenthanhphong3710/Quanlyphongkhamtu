from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class BenhNhanView(ModelView):
    can_edit = True
    column_display_pk = True
    can_view_details = True
    can_set_page_size = 50
    column_labels = dict(benh_nhan_id="Mã bệnh nhân", ho_ten="Họ và tên", gioi_tinh="Gioi tính", nam_sinh="Năm sinh", dia_chi="Địa chỉ")

    column_exclude_list = ['detele_at', 'create_at', ]
    def is_accessible(self):
        return current_user.is_authenticated
