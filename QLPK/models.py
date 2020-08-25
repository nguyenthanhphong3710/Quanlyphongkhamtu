from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin

from QLPK import db


class Phieukhambenh(db.Model):
    phieu_kham_benh_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    ngay_kham = db.Column(db.DateTime, nullable=False)
    trieu_chung = db.Column(db.String(1500))
    benh_nhan_id = db.Column(db.Integer, db.ForeignKey('benhnhan.benh_nhan_id'))
    loai_benh_id = db.Column(db.Integer, db.ForeignKey('loaibenh.loai_benh_id'))
    loai_benh_du_doan_id = db.Column(db.Integer)
    create_at = db.Column(db.DateTime)
    detele_at = db.Column(db.DateTime)


class Chitiethoadon(db.Model):
    hoa_don_id = db.Column(db.Integer, db.ForeignKey('hoadon.hoa_don_id'), primary_key=True)
    thuoc_id = db.Column(db.Integer, db.ForeignKey('thuoc.thuoc_id'), primary_key=True)
    don_vi_id = db.Column(db.Integer, db.ForeignKey('donvi.don_vi_id'), primary_key=True)
    chi_dan_id = db.Column(db.Integer, db.ForeignKey('chidan.chi_dan_id'), primary_key=True)
    so_luong = db.Column(db.Integer)


class Benhnhan(db.Model):
    benh_nhan_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    ho_ten = db.Column(db.String(200))
    gioi_tinh = db.Column(db.Boolean)
    nam_sinh = db.Column(db.DateTime)
    dia_chi = db.Column(db.String(500))
    create_at = db.Column(db.DateTime)
    detele_at = db.Column(db.DateTime, default=None)
    ds_phieu_kham_benh = db.relationship('Phieukhambenh', backref='benh_nhan', lazy=True)


class Hoadon(db.Model):
    hoa_don_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    benh_nhan_id = db.Column(db.Integer, db.ForeignKey('benhnhan.benh_nhan_id'))
    phieu_kham_benh_id = db.Column(db.Integer, db.ForeignKey('phieukhambenh.phieu_kham_benh_id'))
    tien_kham = db.Column(db.Float, nullable=True)
    ngay_thanh_toan = db.Column(db.DateTime)
    tong_tien = db.Column(db.Float)
    ds_chi_tiet_hoa_don = db.relationship('Chitiethoadon', backref='hoa_don', lazy=True)


class Thuoc(db.Model):
    thuoc_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    ten_thuoc = db.Column(db.String(300))
    don_gia = db.Column(db.Float)
    ds_chi_tiet_hoa_don = db.relationship('Chitiethoadon', backref='thuoc', lazy=True)


class Donvi(db.Model):
    don_vi_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    ten_don_vi = db.Column(db.String(300))
    ds_chi_tiet_hoa_don = db.relationship('Chitiethoadon', backref='don_vi', lazy=True)


class Chidan(db.Model):
    chi_dan_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    noi_dung = db.Column(db.String(1500))
    ds_chi_tiet_hoa_don = db.relationship('Chitiethoadon', backref='chi_dan', lazy=True)


class Loaibenh(db.Model):
    loai_benh_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    ten_loai_benh = db.Column(db.String(300))
    ds_phieu_kham_benh = db.relationship('Phieukhambenh', backref='loai_benh', lazy=True)


class Code(db.Model):
    code_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    is_active = db.Column(db.Boolean)
    users = db.relationship('Users',backref='code',lazy=True )

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code_id = db.Column(db.Integer, db.ForeignKey(Code.code_id), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    user_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)

db.create_all()
