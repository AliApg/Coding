import sqlite3 as db
from datetime import datetime
from random import randint

from guizero import *

fnt = 'times new roman'
BG = '#e5f1f1'
title = 'maroon4'
up = 'DarkOrchid4'
light = 'azure'
dark = 'alice blue'


def entry():
    global user_nm, pass_wd, entry_win
    root.hide()
    entry_win = Window(root, 'Entry', width=150, height=205, bg=BG)
    Text(entry_win, '\nUsername', font=fnt)
    user_nm = TextBox(entry_win, width=20)
    Text(entry_win, '\nPassword', font=fnt)
    pass_wd = TextBox(entry_win, width=20, hide_text=True)
    Text(entry_win)
    entry_box = Box(entry_win, layout='grid')
    PushButton(entry_box, lambda: [entry_win.destroy(
    ), admin()], text='Enter', grid=[1, 0], pady=8, width=5)
    PushButton(entry_box, lambda: [entry_win.destroy(
    ), root.show()], text='Back', grid=[0, 0], pady=8, width=5)


def admin():
    global admin_win
    cr.execute('select * from Entry')
    if (tuple([user_nm.value.strip(), pass_wd.value.strip()]) in cr.fetchall()) == True:
        admin_win = Window(root, 'Admin', width=185, bg=BG)
        Text(admin_win)
        PushButton(admin_win, admin_add_item,
                   text='Add items to storage', width=16)
        btn1 = PushButton(admin_win, admin_edit_item,
                          text='Edit storage items', width=16)
        btn2 = PushButton(admin_win, admin_storage_report,
                          text='Storage report', width=16)
        btn3 = PushButton(admin_win, admin_refill_item,
                          text='Refill low number items', width=16)
        PushButton(admin_win, add_admin, text='Add admin', width=16)
        PushButton(admin_win, lambda: [
                   admin_win.destroy(), root.show()], text='Back', width=3)
        cr.execute('select * from Storage')
        btn3.visible = False
        if len(cr.fetchall()) == 0:
            btn1.visible = btn2.visible = False
            admin_win.height = 180
        else:
            btn1.visible = btn2.visible = True
            admin_win.height = 270
            cr.execute('select name,amount from Storage where amount<=5')
            if len(cr.fetchall()) != 0:
                btn3.visible = True
                admin_win.height = 312
    else:
        warn('Incorrect', 'Username or password is incorrect!')
        entry()


def admin_add_item():
    global add_item_win, item_name, item_price, item_qtt
    admin_win.hide()
    add_item_win = Window(admin_win, 'Add item', width=180, height=275, bg=BG)
    Text(add_item_win, '\nItem\'s name', font=fnt)
    item_name = TextBox(add_item_win, width=20)
    Text(add_item_win, '\nItem\'s price', font=fnt)
    item_price = TextBox(add_item_win, width=20)
    Text(add_item_win, '\nItem\'s quantity', font=fnt)
    item_qtt = TextBox(add_item_win, width=20)
    Text(add_item_win)
    add_item_box = Box(add_item_win, layout='grid')
    PushButton(add_item_box, admin_item_check,
               text='Add', grid=[1, 0], width=4, pady=8)
    PushButton(add_item_box, lambda: [admin_win.destroy(
    ), admin()], text='Back', grid=[0, 0], width=4, pady=8)


def admin_item_check():
    add_item_win.hide()
    cr.execute('select name from Storage')
    temp = cr.fetchall()
    if item_name.value.strip() == '':
        warn('Item\'s name', 'Item\'s name cannot be empty!')
        add_item_win.show()
    elif all(not (item_name.value.strip() in i) for i in temp) == False:
        warn('Existing item', 'This item already exists in the storage!')
        add_item_win.show()
    elif item_price.value.strip() == '':
        warn('Item\'s price', 'Item\'s price cannot be empty!')
        add_item_win.show()
    elif item_qtt.value.strip() == '':
        warn('Item\'s quantity', 'Item\'s quantity cannot be empty!')
        add_item_win.show()
    elif item_qtt.value.strip().isdigit() == False:
        warn('Item\'s quantity', 'Item\'s quantity must be a possetive integer number!')
        add_item_win.show()
    elif item_price.value.strip() != '':
        if item_price.value.strip().replace('.', '', 1).isdigit() == True == True and eval(item_price.value.strip()) != 0:
            info(
                'Success', f'"{item_name.value.strip()}" was added to the storage successfully')
            cr.execute(
                f'insert into Storage (name,amount,cost) values ("{item_name.value.strip()}",{int(item_qtt.value.strip())},{float(item_price.value.strip())})')
            storage_db.commit()
            item_name.value = item_price.value = item_qtt.value = ''
            add_item_win.show()
        else:
            warn('Item\'s price', 'Item\'s price must be a possetive number!')
            add_item_win.show()


def admin_edit_item():
    global edit_selection_win, item_to_edit
    admin_win.hide()
    items = []
    cr.execute('select name from Storage')
    temp = cr.fetchall()
    for i in temp:
        items.append(i[0])
    edit_selection_win = Window(
        admin_win, 'Items', width=175, height=165, bg=BG)
    Text(edit_selection_win, '\nSelect the intended item\n', font=fnt)
    item_to_edit = Combo(edit_selection_win, items, width=16)
    Text(edit_selection_win)
    edit_selection_box = Box(edit_selection_win, layout='grid')
    PushButton(edit_selection_box, admin_change_item,
               text='Edit', grid=[2, 0], width=3, pady=7)
    PushButton(edit_selection_box, admin_delete_item,
               text='Delete', grid=[1, 0], width=3, pady=7)
    PushButton(edit_selection_box, lambda: [admin_win.destroy(
    ), admin()], text='Back', grid=[0, 0], width=3, pady=7)


def admin_change_item():
    global change_item_win, changed_item_name, changed_item_price, changed_item_qtt
    edit_selection_win.hide()
    cr.execute(f'select * from Storage where name="{item_to_edit.value}"')
    temp = cr.fetchall()[0]
    change_item_win = Window(
        edit_selection_win, 'Edit item\'s properties', width=180, height=275, bg=BG)
    Text(change_item_win, '\nNew name', font=fnt)
    changed_item_name = TextBox(change_item_win, text=temp[0], width=20)
    Text(change_item_win, '\nNew price', font=fnt)
    changed_item_price = TextBox(change_item_win, text=temp[2], width=20)
    Text(change_item_win, '\nNew quantity', font=fnt)
    changed_item_qtt = TextBox(change_item_win, text=temp[1], width=20)
    Text(change_item_win)
    change_item_box = Box(change_item_win, layout='grid')
    PushButton(change_item_box, lambda: [change_item_win.destroy(
    ), edit_selection_win.show()], text='Back', grid=[0, 0], width=4, pady=8)
    PushButton(change_item_box, admin_change_item_check,
               text='Change', grid=[1, 0], width=4, pady=8)


def admin_change_item_check():
    change_item_win.hide()
    cr.execute(f'select name from Storage where name="{item_to_edit.value}"')
    temp_1 = cr.fetchall()[0]
    cr.execute('select name from Storage')
    temp_2 = cr.fetchall()
    temp_2.remove(temp_1)
    if changed_item_name.value.strip() == '':
        warn('New name', f'Name of the item cannot be empty!')
        change_item_win.show()
    elif all(not (changed_item_name.value.strip() in i) for i in temp_2) == False:
        warn('Existing item',
             f'"{changed_item_name.value.strip()}" already exist in the storage!')
        change_item_win.show()
    elif changed_item_price.value.strip() == '':
        warn('Item\'s price', 'Item\'s price cannot be empty!')
        change_item_win.show()
    elif changed_item_qtt.value.strip() == '':
        warn('Item\'s quantity', 'Item\'s quantity cannot be empty!')
        change_item_win.show()
    elif changed_item_qtt.value.strip().isdigit() == False:
        warn('Item\'s quantity', 'Item\'s quantity must be a possetive integer number!')
        change_item_win.show()
    elif changed_item_price.value.strip() != '':
        if changed_item_price.value.strip().replace('.', '', 1).isdigit() == True and eval(changed_item_price.value.strip()) != 0:
            info(
                'Success', f'"{changed_item_name.value.strip()}" properties was changed successfully')
            cr.execute(
                f'delete from Storage where name="{item_to_edit.value}"')
            cr.execute(
                f'insert into Storage (name,amount,cost) values ("{changed_item_name.value}",{changed_item_qtt.value},{changed_item_price.value})')
            storage_db.commit()
            edit_selection_win.destroy()
            admin_edit_item()
        else:
            warn('Item\'s price', 'Item\'s price must be a possetive number!')
            change_item_win.show()


def admin_delete_item():
    edit_selection_win.hide()
    sure = yesno(
        'Confirm', f'Are you sure you want to delete "{item_to_edit.value}"?')
    if sure == True:
        cr.execute(f'delete from Storage where name="{item_to_edit.value}"')
        info(
            'Success', f'"{item_to_edit.value}" was deleted from the storage successfully')
        admin_win.destroy()
        admin()
    else:
        edit_selection_win.show()


def admin_storage_report():
    admin_win.hide()
    storage_report_win = Window(
        admin_win, 'Storage report', width=566, height=143, layout='grid', bg=BG)
    Text(storage_report_win, grid=[0, 0])
    storage_report_box_1 = Box(
        storage_report_win, layout='grid', grid=[0, 1], border=1)
    Text(storage_report_box_1, 'Product', grid=[
         0, 0], font=fnt, size=20, width=9, color=up, bg=dark)
    Text(storage_report_box_1, 'Quantity', grid=[
         1, 0], font=fnt, size=20, width=9, color=up, bg=light)
    Text(storage_report_box_1, 'Price ($)', grid=[
         2, 0], font=fnt, size=20, width=9, color=up, bg=dark)
    Text(storage_report_box_1, 'Condition', grid=[
         3, 0], font=fnt, size=20, width=9, color=up, bg=light)
    storage_report_box_2 = Box(
        storage_report_win, layout='grid', grid=[0, 2], border=1)
    cr.execute('select * from Storage')
    temp = cr.fetchall()
    x = 0
    for i in temp:
        Text(storage_report_box_2, i[0], grid=[
             0, x], size=12, width=15, font=fnt, bg=light)
        Text(storage_report_box_2, i[1], grid=[
             1, x], size=12, width=15, font=fnt, bg=dark)
        Text(storage_report_box_2, i[2], grid=[
             2, x], size=12, width=15, font=fnt, bg=light)
        if i[1] <= 5:
            condition = 'Very low'
        elif i[1] <= 10:
            condition = 'Low'
        elif i[1] <= 50:
            condition = 'Avrage'
        elif i[1] <= 100:
            condition = 'High'
        else:
            condition = 'Very high'
        Text(storage_report_box_2, condition, grid=[
             3, x], size=12, width=15, font=fnt, bg=dark)
        storage_report_win.height += 26
        x += 1
    Text(storage_report_win, grid=[0, 3])
    PushButton(storage_report_win, lambda: [storage_report_win.destroy(
    ), admin_win.show()], grid=[0, 4], text='OK', width=20, pady=5)


def admin_refill_item():
    global refill_item_win, item_to_fill, amount_of_fill
    admin_win.hide()
    low_items = []
    cr.execute('select name,amount from Storage where amount<=5')
    temp = cr.fetchall()
    for i in temp:
        low_items.append(i[0]+' : '+str(i[1]))
    refill_item_win = Window(admin_win, 'Refill', bg=BG, width=175, height=240)
    Text(refill_item_win, '\nSelect the item to refill\n', font=fnt)
    item_to_fill = Combo(refill_item_win, low_items, width=16)
    Text(refill_item_win, '\nNumber of added items', font=fnt)
    amount_of_fill = TextBox(refill_item_win)
    Text(refill_item_win)
    refill_item_box = Box(refill_item_win, layout='grid')
    PushButton(refill_item_box, admin_refill_check,
               text='Add', grid=[1, 0], width=3, pady=8)
    PushButton(refill_item_box, lambda: [refill_item_win.destroy(
    ), admin_win.show()], text='Back', grid=[0, 0], width=3, pady=8)


def admin_refill_check():
    refill_item_win.hide()
    if amount_of_fill.value.strip().isdigit() == True and amount_of_fill.value.strip() != '0':
        cr.execute(
            f'update Storage set amount=amount+{amount_of_fill.value} where name="{item_to_fill.value.rsplit(" : ",1)[0]}"')
        storage_db.commit()
        info('Success', f'Item addition was successful')
        refill_item_win.destroy()
        admin()
    else:
        warn('Empty', 'Adding amount must be a possetive integer number!')
        refill_item_win.show()


def add_admin():
    global add_admin_win, new_admin_name, new_admin_pass, new_admin_conf
    admin_win.hide()
    add_admin_win = Window(admin_win, 'Add admin',
                           width=150, height=270, bg=BG)
    Text(add_admin_win, '\nUsername', font=fnt)
    new_admin_name = TextBox(add_admin_win, width=20)
    Text(add_admin_win, '\nPassword', font=fnt)
    new_admin_pass = TextBox(add_admin_win, width=20, hide_text=True)
    Text(add_admin_win, '\nConfirm password', font=fnt)
    new_admin_conf = TextBox(add_admin_win, width=20, hide_text=True)
    Text(add_admin_win)
    add_admin_box = Box(add_admin_win, layout='grid')
    PushButton(add_admin_box, admin_check, text='Submit',
               grid=[1, 0], width=4, pady=8)
    PushButton(add_admin_box, lambda: [add_admin_win.destroy(
    ), admin_win.show()], text='Back', grid=[0, 0], width=4, pady=8)


def admin_check():
    add_admin_win.hide()
    cr.execute('select username from Entry')
    temp = cr.fetchall()
    if new_admin_name.value.strip() == '':
        warn('Username', 'Username cannot be empty!')
        add_admin_win.show()
    elif all(not (new_admin_name.value.strip() in i) for i in temp) == False:
        warn('Existing username', 'This username already exists in admins list!')
        add_admin_win.show()
    elif (' ' in new_admin_pass.value.strip()) == True or len(new_admin_pass.value.strip()) < 6:
        warn('Password', 'Password length must be greater than 6 and it cannot contain white space!')
        add_admin_win.show()
    elif new_admin_pass.value.strip() != new_admin_conf.value.strip():
        warn('Confirm password', 'Passwords you entered don\'t match!')
        add_admin_win.show()
    else:
        add_admin_win.destroy()
        cr.execute(
            f'insert into Entry(username,password) values ("{new_admin_name.value.strip()}","{new_admin_pass.value.strip()}")')
        info('Success', f'"{new_admin_name.value.strip()}" is now an admin')
        storage_db.commit()
        admin_win.show()


def user():
    global user_win
    root.hide()
    cr.execute('select * from Users')
    temp = cr.fetchall()
    cr.execute('select * from Storage')
    temp0 = cr.fetchall()
    cr.execute('select * from Storage where amount=0')
    temp1 = cr.fetchall()
    cr.execute('select * from Paid')
    temp2 = cr.fetchall()
    user_win = Window(root, 'User', width=170, height=175, bg=BG)
    Text(user_win)
    order = PushButton(user_win, user_info, text='Order', width=15)
    review = PushButton(user_win, lambda: [user_win.destroy(
    ), user_review()], text='Review previous orders', width=15)
    PushButton(user_win, lambda: [
               user_win.destroy(), root.show()], text='Back', width=15)
    if len(temp1) == len(temp0):
        order.visible = False
        user_win.height -= 40
    else:
        order.visible = True
    if len(temp) == len(temp2) == 0:
        review.visible = False
        user_win.height -= 40
    else:
        review.visible = True
    if order.visible == review.visible == False:
        user_win.destroy()
        warn('Error', 'There is no item to order and no previous order to review!')
        root.show()


def user_info():
    global user_info_win, user_id, fname, lname, gender, age, address
    user_win.destroy()
    user_info_win = Window(root, 'User info', width=210, height=565, bg=BG)
    Text(user_info_win, '\n**If you already have an unpaid**\n*shopping list only enter your ID*\n',
         font=fnt, size=10, color='red')
    Text(user_info_win, 'ID', font=fnt)
    user_id = TextBox(user_info_win, width=20)
    Text(user_info_win, '\nFirstname', font=fnt)
    fname = TextBox(user_info_win, width=20)
    Text(user_info_win, '\nLastname', font=fnt)
    lname = TextBox(user_info_win, width=20)
    Text(user_info_win, '\nGender', font=fnt)
    gender = Combo(user_info_win, [
                   'Prefer not to say', 'Male', 'Female', 'Other'], width=15)
    Text(user_info_win, '\nAge', font=fnt)
    age = Slider(user_info_win, start=10, end=120, width=150)
    Text(user_info_win, '\nAddress', font=fnt)
    address = TextBox(user_info_win, width=20, multiline=True, scrollbar=True)
    Text(user_info_win)
    user_info_box = Box(user_info_win, layout='grid')
    PushButton(user_info_box, user_info_check,
               text='Submit', width=9, pady=8, grid=[1, 0])
    PushButton(user_info_box, lambda: [user_info_win.destroy(
    ), user()], text='Back', width=9, pady=8, grid=[0, 0])


def user_info_check():
    user_info_win.hide()
    cr.execute('select ID from Users')
    temp = cr.fetchall()
    if user_id.value.strip().isdigit() == False or len(user_id.value.strip()) != 10:
        warn('Invalid ID', 'ID must be a 10 digit number!')
        user_info_win.show()
    elif all(user_id.value.strip() not in i for i in temp) == False:
        yn = yesno(
            'Existing id', 'This ID is already in use do you want to continue whith this ID?')
        if yn == True:
            user_order()
        else:
            user_info_win.show()
    elif fname.value.strip() == '':
        warn('Firstname', 'Firstname section cannot be empty!')
        user_info_win.show()
    elif lname.value.strip() == '':
        warn('Lastname', 'Lastname section cannot be empty!')
        user_info_win.show()
    elif address.value.strip() == '':
        warn('Address', 'Address section cannot be empty!')
        user_info_win.show()
    else:
        info('Success', 'Your information submited to the database successfully')
        try:
            cr.execute(
                f'create table "{user_id.value.strip()}" (item text,amount int,cost float)')
        except:
            pass
        cr.execute(
            f'insert into Users (ID,firstname,lastname,gender,age,address,items,total) values ("{user_id.value.strip()}","{fname.value.strip()}","{lname.value.strip()}","{gender.value.strip()}",{age.value},"{address.value.strip()}",0,0)')
        storage_db.commit()
        user_order()


def user_order():
    global user_order_win, ordered_item, item_amount
    cr.execute(f'select items from Users where Id="{user_id.value.strip()}"')
    temp = cr.fetchall()[0][0]
    cr.execute('select name,cost from Storage where amount!=0')
    temp0 = cr.fetchall()
    if temp != 20 and len(temp0) != 0:
        user_order_win = Window(user_info_win, 'Order',
                                width=185, height=230, bg=BG)
        cr.execute('select name,cost from Storage where amount!=0')
        items = (i[0]+' : '+str(i[1]) for i in cr.fetchall())
        Text(user_order_win, '\nSelect the item you need', font=fnt)
        ordered_item = Combo(user_order_win, items, width=20)
        Text(user_order_win, '\nAmount that you need', font=fnt)
        item_amount = Slider(user_order_win, start=1, end=20-temp, width=150)
        Text(user_order_win)
        user_order_box = Box(user_order_win, layout='grid')
        PushButton(user_order_box, user_add_order,
                   text='Add', width=2, pady=8, grid=[3, 0])
        btn1 = PushButton(user_order_box, lambda: [user_order_win.destroy(
        ), user_edit_order()], text='Edit', width=2, pady=8, grid=[1, 0])
        btn2 = PushButton(user_order_box, user_pay, args=[
                          0], text='Pay', width=2, pady=8, grid=[2, 0])
        PushButton(user_order_box, lambda: [user_order_win.destroy(
        ), user_info_win.show()], text='Back', width=2, pady=8, grid=[0, 0])
        if temp == 0:
            btn1.visible = False
            btn2.visible = False
        else:
            btn1.visible = True
            btn2.visible = True
    else:
        if temp == 20:
            a = 'Full'
            b = 'You selectad maximum amount of items!\nDo you want to pay?'
        else:
            a = 'Empty'
            b = 'Storage is empty!\nDo you want to pay?'
        yn = yesno(a, b)
        if yn == False:
            user_edit_order()
        else:
            user_pay(0)


def user_add_order():
    user_order_win.hide()
    cr.execute(
        f'select amount from Storage where name="{ordered_item.value.rsplit(" : ",1)[0]}"')
    temp = cr.fetchall()[0][0]
    cr.execute(
        f'select amount from "{user_id.value.strip()}" where item="{ordered_item.value.rsplit(" : ",1)[0]}"')
    if temp < item_amount.value:
        warn(
            'Storage', f'Unfortunately there is only {temp} "{ordered_item.value.rsplit(" : ",1)[0]}" left in the storage!')
        user_order_win.show()
    else:
        if len(cr.fetchall()) != 0:
            cr.execute(
                f'update "{user_id.value.strip()}" set amount=amount+{item_amount.value} where item="{ordered_item.value.rsplit(" : ",1)[0]}"')
            cr.execute(
                f'update "{user_id.value.strip()}" set cost={float(ordered_item.value.rsplit(" : ",1)[1])} where item="{ordered_item.value.rsplit(" : ",1)[0]}"')
        else:
            cr.execute(
                f'insert into "{user_id.value.strip()}" (item,amount,cost) values ("{ordered_item.value.rsplit(" : ",1)[0]}",{item_amount.value},{float(ordered_item.value.rsplit(" : ",1)[1])})')
        cr.execute(
            f'update Storage set amount=amount-{item_amount.value} where name="{ordered_item.value.rsplit(" : ",1)[0]}"')
        cr.execute(
            f'update Users set items=items+{item_amount.value} where ID="{user_id.value.strip()}"')
        cr.execute(
            f'update Users set total=total+{item_amount.value}*{float(ordered_item.value.rsplit(" : ",1)[1])} where ID="{user_id.value.strip()}"')
        storage_db.commit()
        info(
            'Success', f'{item_amount.value} {ordered_item.value.rsplit(" : ",1)[0]} added to your shopping list successfully')
        user_order_win.destroy()
        user_order()


def user_pay(pay_id):
    global user_pay_win, card1, card2, card3, card4, cvv, pas, code, sec, x_ID, xx_ID
    x_ID = pay_id
    if pay_id == 0:
        pay_id = user_id.value.strip()
        def bk(): return [user_pay_win.destroy(), user_info_win.show()]
        try:
            user_order_win.destroy()
        except:
            pass
    else:
        def bk(): return [user_pay_win.destroy(), user_review()]
        pay_id = chosen_user.value
        try:
            user_review_win.destroy()
        except:
            pass
    cr.execute(f'select total from Users where ID="{pay_id}"')
    temp = cr.fetchall()[0][0]
    xx_ID = pay_id
    if temp != 0:
        user_pay_win = Window(root, 'Payment', width=630, height=685, bg=BG)
        Text(user_pay_win, '\nYour shopping list',
             color=title, font=fnt, size=20)
        user_pay_box = Box(user_pay_win)
        user_pay_box0 = Box(user_pay_box, layout='grid', border=1)
        Text(user_pay_box0, 'Item', grid=[
             0, 0], size=16, color=up, bg=light, font=fnt, width=12)
        Text(user_pay_box0, 'Fee', grid=[
             1, 0], size=16, color=up, bg=dark, font=fnt, width=12)
        Text(user_pay_box0, 'Amount', grid=[
             2, 0], size=16, color=up, bg=light, font=fnt, width=12)
        Text(user_pay_box0, 'Final', grid=[
             3, 0], size=16, color=up, bg=dark, font=fnt, width=12)
        user_pay_box1 = Box(user_pay_box, layout='grid', border=1)
        cr.execute(f'select * from "{pay_id}"')
        ords = cr.fetchall()
        itm = ttl = 0
        for i in range(len(ords)):
            Text(user_pay_box1, ords[i][0], grid=[
                 0, i], size=12, color=up, bg=dark, font=fnt, width=16)
            Text(user_pay_box1, str(
                ords[i][2])+' $', grid=[1, i], size=12, color=up, bg=light, font=fnt, width=16)
            itm += ords[i][1]
            Text(user_pay_box1, str(ords[i][1]), grid=[
                 2, i], size=12, color=up, bg=dark, font=fnt, width=16)
            ttl += ords[i][1]*ords[i][2]
            Text(user_pay_box1, str(ords[i][1]*ords[i][2])+' $', grid=[
                 3, i], size=12, color=up, bg=light, font=fnt, width=16)
            user_pay_win.height += 26
        Text(user_pay_box)
        user_pay_box2 = Box(user_pay_box, layout='grid', border=1)
        Text(user_pay_box2, f'You\'ve selected {itm} items', grid=[
             0, 0], size=14, color=up, bg=light, font=fnt, width=26)
        Text(user_pay_box2, f'Your total is {ttl} $', grid=[
             0, 1], size=14, color=up, bg=dark, font=fnt, width=26)
        Text(user_pay_win, '\nPayment information',
             font=fnt, color=title, size=20)
        user_pay_box3 = Box(user_pay_win, border=1)
        user_pay_box4 = Box(user_pay_box3, layout='grid')
        Text(user_pay_box4, 'Credit card number', font=fnt,
             color=up, size=14, grid=[0, 0, 9, 1])
        Text(user_pay_box4, ' ', size=16, width=1, grid=[0, 1])
        card1 = TextBox(user_pay_box4, grid=[1, 1], width=4)
        Text(user_pay_box4, '-', size=16, width=1, grid=[2, 1])
        card2 = TextBox(user_pay_box4, grid=[3, 1], width=4)
        Text(user_pay_box4, '-', size=16, width=1, grid=[4, 1])
        card3 = TextBox(user_pay_box4, grid=[5, 1], width=4)
        Text(user_pay_box4, '-', size=16, width=1, grid=[6, 1])
        card4 = TextBox(user_pay_box4, grid=[7, 1], width=4)
        Text(user_pay_box4, ' ', size=16, width=1, grid=[8, 1])
        Text(user_pay_box4, '\nCVV2', color=up,
             font=fnt, size=14, grid=[3, 2, 3, 1])
        cvv = TextBox(user_pay_box4, hide_text=True, grid=[3, 3, 3, 1])
        Text(user_pay_box4, '\nPassword', color=up,
             font=fnt, size=14, grid=[3, 4, 3, 1])
        pas = TextBox(user_pay_box4, hide_text=True, grid=[3, 5, 3, 1])
        code = randint(10000, 99999)
        Text(user_pay_box4, '\nSecurity code', color=up,
             font=fnt, size=14, grid=[2, 6, 5, 1])
        Text(user_pay_box4, ''.join([u'{}\u0336'.format(i) for i in str(
            code)]), bg='white', font='BlackCasper', width=5, height=1, size=25, grid=[2, 7, 5, 1])
        sec = TextBox(user_pay_box4, grid=[3, 8, 3, 1])
        Text(user_pay_box4, size=5, grid=[3, 9, 3, 1])
        Text(user_pay_win)
        PushButton(user_pay_win, lambda: [user_pay_win.hide(
        ), user_pay_check()], text='Submit', width=4, pady=8)
        PushButton(user_pay_win, bk, text='Back', width=4, pady=8)
    else:
        warn('Empty', 'There is nothing in your shopping list!')
        user_review()


def user_pay_check():
    print(x_ID)
    c1 = card1.value
    c2 = card2.value
    c3 = card3.value
    c4 = card4.value
    cv = cvv.value
    ps = pas.value
    cd = code
    sc = sec.value
    if all((i.isdigit() and len(i) == 4) for i in [c1, c2, c3, c4]) == False:
        warn('Credit card', 'Credit card number is invalid!')
        user_pay_win.destroy()
        user_pay(x_ID)
        card1.value = c1
        card2.value = c2
        card3.value = c3
        card4.value = c4
    elif cv.isdigit() == False or not (3 <= len(cv) <= 6):
        warn('CVV2', 'CVV2 is invalid please try again!')
        user_pay_win.destroy()
        user_pay(x_ID)
        card1.value = c1
        card2.value = c2
        card3.value = c3
        card4.value = c4
    elif ps.isdigit() == False or not (4 <= len(ps) <= 8):
        warn('Password', 'Password is invalid please try again!')
        user_pay_win.destroy()
        user_pay(x_ID)
        card1.value = c1
        card2.value = c2
        card3.value = c3
        card4.value = c4
        cvv.value = cv
    elif sc != str(cd):
        warn('Security code', 'Security code is incorrect please try again!')
        user_pay_win.destroy()
        user_pay(x_ID)
        card1.value = c1
        card2.value = c2
        card3.value = c3
        card4.value = c4
        cvv.value = cv
        pas.value = ps
    else:
        cr.execute(
            f'alter table "{xx_ID}" rename to "{xx_ID+" "+str(datetime.now()).split(".")[0]}"')
        cr.execute(f'select * from Users where ID="{xx_ID}"')
        cr.execute(
            f'insert into Paid (ID,firstname,lastname,gender,age,address,items,total,trackingcode,date,time) values {cr.fetchall()[0]+(randint(1000000000,9999999999),str(datetime.now()).split(" ")[0],str(datetime.now()).split(" ")[1].split(".")[0])}')
        cr.execute(f'delete from Users where ID="{xx_ID}"')
        storage_db.commit()
        info('Success', 'We hope you enjoyed your shopping experience! :)')
        user_pay_win.destroy()
        user()


def user_edit_order():
    cr.execute(f'select items from Users where Id="{user_id.value.strip()}"')
    temp = cr.fetchall()[0][0]
    if temp == 0:
        user_order()
    else:
        global user_edit_order_win, product
        user_edit_order_win = Window(
            root, 'Edit order', width=175, height=145, bg=BG)
        cr.execute(f'select * from  "{user_id.value.strip()}"')
        itm = [i[0]+' ('+str(i[1])+')' for i in cr.fetchall()]
        user_edit_order_box = Box(user_edit_order_win, layout='grid')
        Text(user_edit_order_box, '\nSelect intended item',
             font=fnt, grid=[0, 0, 3, 1])
        product = Combo(user_edit_order_box, itm, width=20, grid=[0, 1, 3, 1])
        Text(user_edit_order_box, grid=[0, 2])
        PushButton(user_edit_order_box, user_delete_order,
                   text='Delete', width=3, pady=8, grid=[1, 3])
        PushButton(user_edit_order_box, user_change_order,
                   text='Change', width=3, pady=8, grid=[2, 3])
        if temp == 20:
            def bk(): return [user_edit_order_win.destroy(),
                              user_info_win.show()]
        else:
            def bk(): return [user_edit_order_win.destroy(), user_order()]
        PushButton(user_edit_order_box, bk, text='Back',
                   width=3, pady=8, grid=[0, 3])


def user_delete_order():
    user_edit_order_win.hide()
    yn = yesno(
        'Confirm', f'Are you sure you want to delete {product.value.rsplit(" (",1)[0]} from your shopping list?')
    if yn == True:
        cr.execute(
            f'select * from "{user_id.value.strip()}" where item="{product.value.rsplit(" (",1)[0]}"')
        temp = cr.fetchall()[0]
        cr.execute(
            f'update Storage set amount=amount+{temp[1]} where name="{product.value.rsplit(" (",1)[0]}"')
        cr.execute(
            f'update Users set items=items-{temp[1]} where ID="{user_id.value.strip()}"')
        cr.execute(
            f'update Users set total=total-{temp[1]*temp[2]} where ID="{user_id.value.strip()}"')
        cr.execute(
            f'delete from "{user_id.value.strip()}" where item="{product.value.rsplit(" (",1)[0]}"')
        storage_db.commit()
        info(
            'Success', f'{product.value.rsplit(" (",1)[0]} removed from your shopping list successfully')
        user_edit_order_win.destroy()
        user_edit_order()
    else:
        user_edit_order_win.show()


def user_change_order():
    global user_change_order_win, changed_amount
    user_edit_order_win.hide()
    cr.execute(f'select items from Users where ID="{user_id.value.strip()}"')
    al = cr.fetchall()[0][0]
    cr.execute(
        f'select amount from "{user_id.value.strip()}" where item="{product.value.rsplit(" (",1)[0]}"')
    it = cr.fetchall()[0][0]
    user_change_order_win = Window(
        user_edit_order_win, 'Change', width=165, height=195, bg=BG)
    Text(user_change_order_win, '\n'+product.value, font=fnt)
    changed_amount = Slider(user_change_order_win, start=1, end=20-al+it)
    Text(user_change_order_win)
    PushButton(user_change_order_win, user_change_order_check,
               text='Change', width=8, pady=6)
    PushButton(user_change_order_win, lambda: [user_change_order_win.destroy(
    ), user_edit_order_win.show()], text='Back', width=8, pady=6)


def user_change_order_check():
    user_change_order_win.hide()
    cr.execute(
        f'select amount from Storage where name="{product.value.rsplit(" (",1)[0]}"')
    st = cr.fetchall()[0][0]
    cr.execute(
        f'select amount from "{user_id.value.strip()}" where item="{product.value.rsplit(" (",1)[0]}"')
    oa = cr.fetchall()[0][0]
    if changed_amount.value > oa+st:
        warn(
            'Fail', f'There is only {oa+st} "{product.value.rsplit(" (",1)[0]}" left!')
        user_change_order_win.show()
    else:
        cr.execute(
            f'select cost from "{user_id.value.strip()}" where item="{product.value.rsplit(" (",1)[0]}"')
        oc = cr.fetchall()[0][0]
        cr.execute(
            f'update Storage set amount=amount+{oa-changed_amount.value} where name="{product.value.rsplit(" (",1)[0]}"')
        cr.execute(
            f'update "{user_id.value.strip()}" set amount={changed_amount.value} where item="{product.value.rsplit(" (",1)[0]}"')
        cr.execute(
            f'select cost from Storage where name="{product.value.rsplit(" (",1)[0]}"')
        nc = cr.fetchall()[0][0]
        cr.execute(
            f'update "{user_id.value.strip()}" set cost={nc} where item="{product.value.rsplit(" (",1)[0]}"')
        cr.execute(
            f'update Users set items=items+{changed_amount.value-oa} where ID="{user_id.value.strip()}"')
        cr.execute(
            f'update Users set total=total+{(changed_amount.value*nc)-(oa*oc)} where ID="{user_id.value.strip()}"')
        storage_db.commit()
        info(
            'Success', f'Now you have {changed_amount.value} "{product.value.rsplit(" (",1)[0]}" in your shoppig list')
        user_edit_order_win.destroy()
        user_edit_order()


def user_review():
    global user_review_win, chosen_user
    cr.execute('select ID from Users')
    temp = cr.fetchall()
    ids = [i[0] for i in temp]
    user_review_win = Window(root, 'Review', width=170, height=260, bg=BG)
    a = Text(user_review_win, '\nChoose intended ID', font=fnt)
    b = chosen_user = Combo(user_review_win, ids, width=16)
    Text(user_review_win)
    user_review_box = Box(user_review_win, layout='grid')
    PushButton(user_review_box, user_show_all, text='Show all orders',
               grid=[0, 0, 2, 1], width=16, pady=7)
    c = PushButton(user_review_box, user_show, text='Show',
                   grid=[1, 1], width=6, pady=7)
    d = PushButton(user_review_box, user_edit, text='Edit',
                   grid=[0, 1], width=6, pady=7)
    e = PushButton(user_review_box, user_delete,
                   text='Delete', grid=[0, 2], width=6, pady=7)
    f = PushButton(user_review_box, user_pay, args=[
                   1], text='Pay', grid=[1, 2], width=6, pady=7)
    PushButton(user_review_box, lambda: [user_review_win.destroy(
    ), user()], text='Back', grid=[0, 3, 2, 1], width=16, pady=7)
    if len(temp) == 0:
        user_review_win.height -= 135
        for i in [a, b, c, d, e, f]:
            i.visible = False


def user_show():
    user_review_win.hide()
    user_show_win = Window(
        user_review_win, chosen_user.value, width=1525, height=200, bg=BG)
    Text(user_show_win, '\nUser\'s information', font=fnt, size=20, color=title)
    user_show_box1 = Box(user_show_win, layout='grid', border=1)
    temp = ['ID', 'Firstname', 'Lastname', 'Gender',
            'Age', 'Address', 'Number of items', 'Total $']
    clr = [dark, light]*4
    for j in range(2):
        for i in range(len(temp)):
            Text(user_show_box1, temp[i], font=fnt, size=12,
                 color=up, bg=clr[i], grid=[i, j], width=20)
        if j == 0:
            cr.execute(f'select * from Users where id="{chosen_user.value}"')
            temp = cr.fetchall()[0]
            clr = [light, dark]*4
    if temp[-2] != 0:
        user_show_win.height += 120
        Text(user_show_win, '\nUser\'s order', font=fnt, size=20, color=title)
        user_show_box2 = Box(user_show_win, layout='grid')
        user_show_box3 = Box(user_show_box2, layout='grid',
                             grid=[0, 0], border=1)
        Text(user_show_box3, 'Item\'s name', size=12, color=up,
             bg=dark, font=fnt, grid=[0, 0], width=12)
        Text(user_show_box3, 'Amount', size=12, color=up,
             bg=light, font=fnt, grid=[0, 1], width=12)
        user_show_box4 = Box(user_show_box2, layout='grid',
                             grid=[1, 0], border=1)
        cr.execute(f'select * from "{chosen_user.value}"')
        temp = cr.fetchall()
        for i in range(len(temp)):
            Text(user_show_box4, temp[i][0], size=12, color=up, bg=light, grid=[
                 i, 0], font=fnt, width=12)
            Text(user_show_box4, temp[i][1], size=12, color=up, bg=dark, grid=[
                 i, 1], font=fnt, width=12)
    Text(user_show_win)
    PushButton(user_show_win, lambda: [user_show_win.destroy(
    ), user_review_win.show()], text='OK', width=30, pady=7)


def user_show_all():
    user_review_win.hide()
    user_show_all_win = Window(
        user_review_win, 'All user\s information', width=1525, height=90, bg=BG)
    cr.execute('select * from Users')
    tempu = cr.fetchall()
    cr.execute('select * from Paid')
    tempp = cr.fetchall()
    if len(tempu) != 0:
        user_show_all_win.height += 90
        Text(user_show_all_win, '\nUsers information',
             font=fnt, size=20, color=title)
        user_show_all_box1 = Box(user_show_all_win, layout='grid', border=1)
        temp = ['ID', 'Firstname', 'Lastname', 'Gender',
                'Age', 'Address', 'Number of items', 'Total $']
        clr = [dark, light]*4
        for i in range(len(temp)):
            Text(user_show_all_box1, temp[i], font=fnt, size=12, color=up, bg=clr[i], grid=[
                 i, 0], width=20)
        cr.execute('select * from Users')
        temp = cr.fetchall()
        clr = [light, dark]*4
        for i in range(len(temp)):
            for j in range(len(temp[i])):
                Text(user_show_all_box1, temp[i][j], font=fnt, size=12, color=up, bg=clr[j], grid=[
                     j, i+1], width=20)
            user_show_all_win.height += 30
    if len(tempp) != 0:
        user_show_all_win.height += 85
        user_show_all_win.width += 75
        Text(user_show_all_win, '\nPaid users information',
             font=fnt, size=20, color=title)
        user_show_all_box2 = Box(user_show_all_win, layout='grid', border=1)
        temp = ['ID', 'Firstname', 'Lastname', 'Gender', 'Age', 'Address',
                'Number of items', 'Total $', 'Tracking code', 'Date', 'Time']
        clr = [dark, light]*6
        for i in range(len(temp)):
            Text(user_show_all_box2, temp[i], font=fnt, size=10, color=up, bg=clr[i], grid=[
                 i, 0], width=19)
        cr.execute('select * from Paid')
        temp = cr.fetchall()
        clr = [light, dark]*6
        for i in range(len(temp)):
            for j in range(len(temp[i])):
                Text(user_show_all_box2, temp[i][j], font=fnt, size=10, color=up, bg=clr[j], grid=[
                     j, i+1], width=19)
            user_show_all_win.height += 28
    Text(user_show_all_win)
    PushButton(user_show_all_win, lambda: [user_show_all_win.destroy(
    ), user_review_win.show()], text='OK', width=30, pady=7)


def user_edit():
    global user_edit_win, user_id, fname, lname, gender, age, address
    user_review_win.hide()
    cr.execute(f'select * from Users where ID="{chosen_user.value}"')
    temp = cr.fetchall()[0]
    user_edit_win = Window(user_review_win, 'User info',
                           width=210, height=500, bg=BG)
    Text(user_edit_win, 'ID', font=fnt)
    user_id = TextBox(user_edit_win, text=chosen_user.value, width=20)
    Text(user_edit_win, '\nFirstname', font=fnt)
    fname = TextBox(user_edit_win, text=temp[1], width=20)
    Text(user_edit_win, '\nLastname', font=fnt)
    lname = TextBox(user_edit_win, text=temp[2], width=20)
    Text(user_edit_win, '\nGender', font=fnt)
    gender = Combo(user_edit_win, [
                   'Prefer not to say', 'Male', 'Female', 'Other'], width=15)
    gender.value = temp[3]
    Text(user_edit_win, '\nAge', font=fnt)
    age = Slider(user_edit_win, start=10, end=120, width=150)
    age.value = temp[4]
    Text(user_edit_win, '\nAddress', font=fnt)
    address = TextBox(
        user_edit_win, text=temp[5], width=20, multiline=True, scrollbar=True)
    Text(user_edit_win)
    user_info_box = Box(user_edit_win, layout='grid')
    PushButton(user_info_box, user_edit_check,
               text='Submit', width=9, pady=8, grid=[1, 0])
    PushButton(user_info_box, lambda: [user_edit_win.destroy(
    ), user_review_win.show()], text='Back', width=9, pady=8, grid=[0, 0])


def user_edit_check():
    user_edit_win.hide()
    cr.execute('select ID from Users')
    temp = cr.fetchall()
    temp.remove((chosen_user.value,))
    temp += [('distraction',)]
    if user_id.value.strip().isdigit() == False or len(user_id.value.strip()) != 10:
        warn('Invalid ID', 'ID must be a 10 digit number try again!')
        user_edit_win.show()
    elif all(user_id.value.strip() not in i[0] for i in temp) == False:
        warn('Existing id', 'This ID is already in use try again!')
        user_edit_win.show()
    elif fname.value.strip() == '':
        warn('Firstname', 'Firstname section cannot be empty try again!')
        user_edit_win.show()
    elif lname.value.strip() == '':
        warn('Lastname', 'Lastname section cannot be empty try again!')
        user_edit_win.show()
    elif address.value.strip() == '':
        warn('Address', 'Address section cannot be empty try again!')
        user_edit_win.show()
    else:
        cr.execute(f'update  Users set ID="{user_id.value.strip()}",firstname="{fname.value.strip()}",lastname="{lname.value.strip()}",gender="{gender.value.strip()}",age={age.value},address="{address.value.strip()}" where ID="{chosen_user.value}"')
        try:
            cr.execute(
                f'alter table "{chosen_user.value}" rename to "{user_id.value.strip()}"')
        except:
            pass
        storage_db.commit()
        info('Success', 'Your information successfully updated')
        user_review_win.destroy()
        user_review()


def user_delete():
    user_review_win.hide()
    yn = yesno(
        'Confirm', f'Are you sure you want to delete user "{chosen_user.value}"?')
    if yn == True:
        cr.execute(f'drop table "{chosen_user.value}"')
        cr.execute(f'delete from Users where ID="{chosen_user.value}"')
        storage_db.commit()
        info(
            'Success', f'User {chosen_user.value} information and shopping list deleted successfully')
        user_review_win.destroy()
        user()
    else:
        user_review_win.show()


storage_db = db.connect('StorageApp.db')
cr = storage_db.cursor()
try:
    cr.execute('create table Entry (username text,password text)')
    cr.execute('create table Storage (name text,amount int,cost float)')
    cr.execute('create table Users (ID text,firstname text,lastname text,gender text,age int,address text,items int,total float)')
    cr.execute('create table Paid (ID text,firstname text,lastname text,gender text,age int,address text,items int,total float,trackingcode int,date text,time text)')
    cr.execute('insert into Entry (username,password) values ("admin","123456")')
    storage_db.commit()
except:
    pass
root = App('Storage', width=165, height=150, bg=BG)
root_box = Box(root, layout='grid')
Text(root_box, '\nWelcome to Storage!\n',
     color=title, font=fnt, grid=[0, 0, 2, 1])
PushButton(root_box, entry, text='Admin', width=6, pady=6, grid=[0, 1])
PushButton(root_box, user, text='User', width=6, pady=6, grid=[1, 1])
PushButton(root_box, root.destroy, text='Exit',
           width=16, pady=6, grid=[0, 2, 2, 1])
root.display()
