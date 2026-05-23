from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

auto_reply = {
    "harga": "Harga produk mulai dari 50 ribu.",
    "lokasi": "Kami berada di Jakarta, Indonesia.",
    "jam buka": "Kami buka jam 09:00 sampai 21:00.",
    "buka": "Kami buka jam 09:00 sampai 21:00.",
    "order": "Untuk memesan, silakan hubungi customer service kami.",
    "cod": "Kami menerima pembayaran COD di area Jakarta.",
    "terima kasih": "Sama-sama! Jika ada pertanyaan lain, silakan tanya.",
    "makasih": "Sama-sama! Jika ada pertanyaan lain, silakan tanya.",
    "halo": "Halo! Ada yang bisa saya bantu hari ini?",
}

def ai_response(text):

    try:
        response = client.chat.completions.create(
            model = "llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. "
                "answer the user's question on Indonesia language."
                " Answer in a short sentence and be concise."},
                {"role": "user", "content": text}
            ]
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("AI Error:", e)
        return "Sorry, I'm having trouble right now."


def read_last_message():
    messages = driver.find_elements(
        By.CSS_SELECTOR,
        "div.message-in span.copyable-text"
    )

    if messages:
        return messages[-1].text.strip()
    return None


def main():
    driver = webdriver.Edge()

    driver.get("https://web.whatsapp.com")

    print("Please scan the QR Code...")

    WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.ID, "pane-side"))
    )

    print("WhatsApp Successfully logged in.")
    print("Please open the chat you want to interact with.")

    input("Press ENTER after opening the chat...")

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.message-in"))
    )

    print("Bot is now active.")
    last_message = ""

    while True:
        
        try:

            unread_chats = driver.find_elements(
                By.CSS_SELECTOR,
                "span[aria-label*='unread']"
            )

            if unread_chats:
                print("There is a new message")
                unread_chats[0].click()
                time.sleep(2)

                last_message = ""
                messages = read_last_message()
                
                print("Bot is checking the message...")

            messages = driver.find_elements(
                By.CSS_SELECTOR,
                "div.message-in span.copyable-text"
            )

            print("Number of messages detected:", len(messages))

            if messages:
                current_last = messages[-1].text.strip()

                print("Last message read:", current_last)

                if current_last != last_message:
                    print("New message:", current_last)
                    lower_msg = current_last.lower()
                    reply = None

                    for keyword in auto_reply:
                        if keyword in lower_msg:
                            reply = auto_reply[keyword]
                            break

                    if reply is None:
                        print("Using AI...")
                        reply = ai_response(current_last)

                    time.sleep(1)

                    input_box = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, "footer div[contenteditable='true']")
                        )
                    )

                    input_box.send_keys(reply)
                    input_box.send_keys(Keys.ENTER)

                    print("Bot is replying:", reply)

                    last_message = current_last

        except Exception as e:

            print("An error occurred:", e)

        time.sleep(5)

if __name__ == "__main__":
    main()