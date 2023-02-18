import frappe

def calc_hours(doc,method):
    work_hours=0
    if doc.check_out and doc.check_in:
        hours =frappe.utils.time_diff_in_hours(doc.check_out,doc.check_in)
        work_hours=float(hours)

    doc.work_hours=work_hours

def status_assign(doc,method):
    if not (doc.check_out and doc.check_in):
        doc.status="Absent"