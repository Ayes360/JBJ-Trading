from flask import Blueprint, render_template

general = Blueprint("general", __name__)

@general.get("/")
def index():
    return render_template("index.html")

@general.get("/login")
def login():
    return render_template("login.html")

@general.get("/all-orders")
def all_orders():
    return render_template("sales/all-orders.html")

@general.get("/drafts")
def drafts():
    return render_template("sales/drafts.html")

@general.get("/create-order")
def create_order():
    return render_template("sales/create-order.html")

@general.get("/create-bso")
def create_bso():
    return render_template("warehouse/create-bso.html")

@general.get("/all-bso")
def all_bso():
    return render_template("warehouse/all-bso.html")

@general.get("/stock-all")
def stock_all():
    return render_template("warehouse/stock-all.html")

@general.get("/all-products")
def all_products():
    return render_template("products/all-products.html")

@general.get("/bodega-out-detail")
def bodega_out_detail():
    return render_template("warehouse/bodega-out-detail.html")

@general.get("/order-update")
def order_update():
    return render_template("sales/order-update.html")

@general.get("/itemized")
def itemized():
    return render_template("sales/itemized.html")

@general.get("/stock-transfer")
def stock_transfer():
    return render_template("warehouse/stock-transfer.html")

@general.get("/itemized-bso")
def itemized_bso():
    return render_template("warehouse/itemized-bso.html")

@general.get("/create-new-product")
def create_new_product():
    return render_template("products/create-new-product.html")

@general.get("/All-Invoices/all-invoice")
def all_invoice():
    return render_template("products/All-Invoices/all-invoice.html")

@general.get("/All-Invoices/add-new-invoice")
def add_new_invoice():
    return render_template("products/All-Invoices/add-new-invoice.html")

@general.get("/All-Invoices/invoice-details")
def invoice_details():
    return render_template("products/All-Invoices/invoice-details.html")

@general.get("/payment/all-payments")
def all_payments():
    return render_template("products/payment/all-payments.html")

@general.get("/payment/add-new-payment")
def add_new_payment():
    return render_template("products/payment/add-new-payment.html")

@general.get("/supplier/new-supplier")
def new_supplier():
    return render_template("products/supplier/new-supplier.html")

@general.get("/supplier/add-new-supplier")
def add_new_supplier():
    return render_template("products/supplier/add-new-supplier.html")

@general.get("/customer/customer-list")
def customer_list():
    return render_template("/customer/customer-list.html")

@general.get("/receive-payment/add-payment")
def add_payment():
    return render_template("customer/receive-payment/add-payment.html")

@general.get("/receive-payment/customer-payment")
def customer_payment():
    return render_template("customer/receive-payment/customer-payment.html")

@general.get("/customer/add-new-customer")
def add_new_customer():
    return render_template("customer/add-new-customer.html")

@general.get("/warehouse/product-detail")
def product_detail():
    return render_template("/warehouse/product-detail.html")