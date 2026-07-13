import turtle
import time

# স্ক্রিন সেটআপ
screen = turtle.Screen()
screen.setup(width=600, height=700)
screen.title("Perfect Flower Animation")
screen.bgcolor("#0b253a")  # ছবির মতো রিয়ালিস্টিক ব্যাকগ্রাউন্ড

t = turtle.Turtle()
t.speed(0)
turtle.delay(5)

# ১. ডাটা এবং পাতা আঁকা (একদম পারফেক্ট পজিশনে)
def draw_stem_and_leaves():
    t.penup()
    t.goto(0, -320)
    t.pendown()
    t.color("#3da652")  
    t.pensize(10)
    t.setheading(90)
    t.forward(320)  # ডাটা (স্টেম) কেন্দ্রের নিচে গিয়ে থামবে
    
    # বামের পাতা
    t.penup()
    t.goto(0, -120)
    t.setheading(140)
    t.pendown()
    t.begin_fill()
    t.circle(60, 90)
    t.left(90)
    t.circle(60, 90)
    t.end_fill()
    
    # ডানের পাতা
    t.penup()
    t.goto(0, -100)
    t.setheading(40)
    t.pendown()
    t.begin_fill()
    t.circle(-60, 90)
    t.right(90)
    t.circle(-60, 90)
    t.end_fill()

# ২. নিখুঁত পাপড়ি আঁকার ফাংশন
def draw_petal():
    t.color("#ff9100", "#ffaa00")  # বর্ডার কমলা, ভেতরে উজ্জ্বল হলুদ/কমলা
    t.begin_fill()
    # একটি সুন্দর সূক্ষ্ম উপবৃত্তাকার বা পাতা আকৃতির পাপড়ি
    for _ in range(2):
        t.circle(120, 40)   # ব্যাসার্ধ ১২০, চাপ ৪০ ডিগ্রি
        t.left(140)         # সূক্ষ্ম কোণ করার জন্য ঘুরে যাওয়া
    t.end_fill()

# ৩. ফুল অ্যানিমেশন (কোনো বাগ বা বাইরে চলে যাওয়ার চান্স নেই)
def draw_full_flower():
    # প্রতিবার কেন্দ্র (0, 0) থেকে পাপড়ি শুরু হবে
    for angle in range(0, 360, 12):  # ১২ ডিগ্রি পরপর মোট ৩০টি ঘন পাপড়ি
        t.penup()
        t.goto(0, 0)         # প্রতিবার কেন্দ্রে ফেরত আসবে, তাই ফুল সরবে না
        t.setheading(angle)  # সঠিক কোণে ঘুরবে
        t.pendown()
        draw_petal()
        time.sleep(0.02)     # অ্যানিমেশন ইফেক্ট
        
    # ৪. ফুলের মাঝখানের ডার্ক গোল অংশ
    t.penup()
    t.goto(0, -45) 
    t.setheading(0)
    
    # বড় খয়েরি অংশ
    t.color("#522207")
    t.pendown()
    t.begin_fill()
    t.circle(45)
    t.end_fill()
    
    # ভেতরের ডার্ক শ্যাডো অংশ
    t.penup()
    t.goto(0, -32)
    t.color("#210c01")
    t.pendown()
    t.begin_fill()
    t.circle(32)
    t.end_fill()

# মেইন প্রোগ্রাম
draw_stem_and_leaves()
draw_full_flower()

t.hideturtle()
screen.mainloop()
