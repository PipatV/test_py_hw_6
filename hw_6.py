# ข้อ 6 สุ่มไพ่

#นำมาเพื่อใช้สำหรับสุ่ม
import random

# ตัวแปร cards เก็บแบบ dictionary
cards = {
    # 1 = Ace
    "Ace_ดอกจิก": 1,
    "Ace_ข้าวหลามตัด": 1,
    "Ace_หัวใจ": 1,
    "Ace_โพดำ": 1,

    # 11 = Jack
    "Jack_ดอกจิก": 11,
    "Jack_ข้าวหลามตัด": 11,
    "Jack_หัวใจ": 11,
    "Jack_โพดำ": 11,

    # 12 = Queen
    "Queen_ดอกจิก": 12,
    "Queen_ข้าวหลามตัด": 12,
    "Queen_หัวใจ": 12,
    "Queen_โพดำ": 12,

    # 13 = King
    "King_ดอกจิก": 12,
    "King_ข้าวหลามตัด": 12,
    "King_หัวใจ": 12,
    "King_โพดำ": 12,


    "2_ดอกจิก": 2,
    "2_ข้าวหลามตัด": 2,
    "2_หัวใจ": 2,
    "2_โพดำ": 2,

    "3_ดอกจิก": 3,
    "3_ข้าวหลามตัด": 3,
    "3_หัวใจ": 3,
    "3_โพดำ": 3,

    "4_ดอกจิก": 4,
    "4_ข้าวหลามตัด": 4,
    "4_หัวใจ": 4,
    "4_โพดำ": 4,

    "5_ดอกจิก": 5,
    "5_ข้าวหลามตัด": 5,
    "5_หัวใจ": 5,
    "5_โพดำ": 5,

    "6_ดอกจิก": 6,
    "6_ข้าวหลามตัด": 6,
    "6_หัวใจ": 6,
    "6_โพดำ": 6,

    "7_ดอกจิก": 7,
    "7_ข้าวหลามตัด": 7,
    "7_หัวใจ": 7,
    "7_โพดำ": 7,

    "8_ดอกจิก": 8,
    "8_ข้าวหลามตัด": 8,
    "8_หัวใจ": 8,
    "8_โพดำ": 8,
    
    "9_ดอกจิก": 9,
    "9_ข้าวหลามตัด": 9,
    "9_หัวใจ": 9,
    "9_โพดำ": 9,

    "10_ดอกจิก": 10,
    "10_ข้าวหลามตัด": 10,
    "10_หัวใจ": 10,
    "10_โพดำ": 10,


}

# สุ่ม dictionary ภายในตัวแปร cards ลงในตัวแปร first_cards
first_cards = random.choice(list(cards.items()))

# สุ่ม dictionary ภายในตัวแปร cards ลงในตัวแปร second_cards
second_cards = random.choice(list(cards.items()))

# ดึงค่า จากตัวแปรทั้งสองตัวผ่่าน index
sum_cards = first_cards[1] + second_cards [1]

# แสดงค่าออกไป
print(first_cards)
print(second_cards)
print(sum_cards)

