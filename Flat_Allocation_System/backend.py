import mysql.connector
from db_config import db_config

# ---------- CONNECTION ----------
def get_connection():
    return mysql.connector.connect(**db_config)

# ---------- FLATS ----------
def get_flats():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT flat_id, flat_number, floor, flat_type, rent_amount, status
        FROM Flat
    """)
    rows = cur.fetchall()
    conn.close()
    return rows

# ---------- TENANTS ----------
def get_tenants():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT tenant_id, name, phone, id_proof, join_date
        FROM Tenant
    """)
    rows = cur.fetchall()
    conn.close()
    return rows

def add_tenant(name, phone, id_proof, join_date):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Tenant (name, phone, id_proof, join_date)
        VALUES (%s, %s, %s, %s)
    """, (name, phone, id_proof, join_date))
    conn.commit()
    conn.close()

# ---------- ALLOCATION ----------
def allocate_flat(tenant_id, flat_id, start_date):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO Allocation (tenant_id, flat_id, start_date)
        VALUES (%s, %s, %s)
    """, (tenant_id, flat_id, start_date))

    cur.execute("""
        UPDATE Flat
        SET status = 'Occupied'
        WHERE flat_id = %s
    """, (flat_id,))

    conn.commit()
    conn.close()

# ---------- PAYMENT ----------
def add_payment(tenant_id, month, amount, status):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Payment (tenant_id, month, amount, status)
        VALUES (%s, %s, %s, %s)
    """, (tenant_id, month, amount, status))
    conn.commit()
    conn.close()
# ---------- PAYMENTS ----------
def get_payments():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            p.payment_id,
            t.name,
            p.month,
            p.amount,
            p.status
        FROM Payment p
        JOIN Tenant t ON p.tenant_id = t.tenant_id
    """)
    rows = cur.fetchall()
    conn.close()
    return rows
