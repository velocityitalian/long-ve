"""VELOCITY LONGFORM - 16:9 chapter lesson, brand and motion constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1920
VIDEO_HEIGHT = 1080
FPS = 30

TARGET_CHAPTERS = 8
PHRASES_PER_CHAPTER = 7
TARGET_PHRASES = TARGET_CHAPTERS * PHRASES_PER_CHAPTER

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY VIETNAMESE"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "VIETNAMESE"
HANDLE = "@velocityvietnamese"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {'code': 'vi',
 'name': 'Vietnamese',
 'native_name': 'Tiếng Việt',
 'history_key': 'vietnamese',
 'english_voice': 'en-US-AvaNeural',
 'english_fallback_voice': 'en-US-GuyNeural',
 'native_voice': 'vi-VN-HoaiMyNeural',
 'native_fallback_voice': 'vi-VN-NamMinhNeural',
 'native_engine': 'edge',
 'native_lang_code': 'vi',
 'english_rate': '-4%',
 'native_rate': '-10%',
 'english_pitch': '+0Hz',
 'native_pitch': '+0Hz',
 'native_label': 'TIẾNG VIỆT',
 'translit_label': 'SAY IT LIKE',
 'flag': 'vn',
 'greeting': 'Xin chào!',
 'encouragement': 'Tuyệt vời!',
 'rtl': False,
 'char_tiles': False,
 'script_font': '',
 'glyphs': 'AĂÂBCDĐEÊGHIKLMNOÔƠPQRSTUƯVXYaăâbcdđeêghiklmnoôơpqrstuưvxy'}
# ==== LANGUAGE PACK END ====

# ==== CATEGORIES START ====
CATEGORIES = {'Motivation': 'Động lực',
 'Love': 'Tình yêu',
 'Success': 'Thành công',
 'Wisdom': 'Trí tuệ',
 'Happiness': 'Hạnh phúc',
 'Self Improvement': 'Phát triển bản thân',
 'Gratitude': 'Lòng biết ơn',
 'Friendship': 'Tình bạn',
 'Hope': 'Hy vọng',
 'Creativity': 'Sáng tạo',
 'Inner Peace': 'Bình an nội tâm',
 'Confidence': 'Tự tin',
 'Perseverance': 'Kiên trì',
 'Inspiration': 'Cảm hứng',
 'Positive Life': 'Cuộc sống tích cực',
 'Courage': 'Can đảm',
 'Kindness': 'Tử tế',
 'Patience': 'Kiên nhẫn',
 'Forgiveness': 'Tha thứ',
 'Strength': 'Sức mạnh',
 'Joy': 'Niềm vui',
 'Balance': 'Cân bằng',
 'Growth': 'Phát triển',
 'Purpose': 'Mục đích',
 'Mindfulness': 'Chánh niệm',
 'Travel & Airport': 'Du lịch & Sân bay',
 'Ordering Food & Dining': 'Đặt món & Ăn uống',
 'Shopping & Prices': 'Mua sắm & Giá cả',
 'Asking for Directions': 'Hỏi đường',
 'Hotel & Accommodation': 'Khách sạn & Chỗ ở',
 'Daily Routine': 'Sinh hoạt hàng ngày',
 'Meeting People & Greetings': 'Gặp gỡ & Chào hỏi',
 'Emergency & Health': 'Khẩn cấp & Sức khỏe',
 'Public Transportation': 'Phương tiện công cộng',
 'Work & Office': 'Công việc & Văn phòng',
 'Weather & Small Talk': 'Thời tiết & Chuyện phiếm',
 'Coffee Shop & Bakery': 'Quán cà phê & Tiệm bánh',
 'Family & Home': 'Gia đình & Nhà cửa',
 'Hobbies & Free Time': 'Sở thích & Thời gian rảnh',
 'Dating & Romance': 'Hẹn hò & Tình yêu',
 'Phone Calls & Messages': 'Gọi điện & Tin nhắn',
 'Banking & Money': 'Ngân hàng & Tiền bạc',
 'Doctor & Pharmacy': 'Bác sĩ & Nhà thuốc',
 'Sports & Fitness': 'Thể thao & Thể hình',
 'Celebrations & Parties': 'Lễ hội & Tiệc tùng',
 'Feelings & Emotions': 'Cảm xúc',
 'Agreeing & Disagreeing': 'Đồng ý & Không đồng ý',
 'Making Plans': 'Lên kế hoạch',
 'Common Native Slang': 'Tiếng lóng thông dụng',
 'Cultural Traditions': 'Truyền thống văn hóa'}
# ==== CATEGORIES END ====

CATEGORY_NAMES = list(CATEGORIES.keys())

AI_MODEL = os.getenv("AI_MODEL", "openai/gpt-5.4-nano")
AI_FALLBACK_MODEL = os.getenv("AI_FALLBACK_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 7.2
CHAPTER_INTRO_DURATION = 4.4
OUTRO_DURATION = 13.0

EN_CARD_IN = 0.70
GAP_EN_NATIVE = 0.60
NATIVE_CARD_LEAD = 0.40
GAP_BEFORE_REPEAT = 1.00
TAIL_HOLD = 1.30

# ---------------------------------------------------------------- palette

INK = "#30303A"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#7C5CFF"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

# ==== HASHTAGS START ====
HASHTAGS = ['#learnvietnamese',
 '#vietnameselessons',
 '#vietnameseforbeginners',
 '#languagelearning',
 '#vietnamesevocabulary',
 '#velocityvietnamese',
 '#dailyvietnamese',
 '#vietnamese',
 '#learnlanguages',
 '#speakvietnamese']
# ==== HASHTAGS END ====
