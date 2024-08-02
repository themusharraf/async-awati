# Python da async va await

- Python dasturlash tilida `async` va `await` kalit so'zlari asinxron dasturlashni amalga oshirish uchun ishlatiladi.
  Asinxron dasturlash bir vaqtning o'zida bir nechta ishlarni bajarishga imkon beradi va ayniqsa kutilayotgan
  kirish-chiqish `(I/O)` input-output operatsiyalari bilan ishlashda samarali hisoblanadi.

---

## (I/O) Input-Output

  ![165px-Operating_system_placement](https://github.com/user-attachments/assets/819c67fe-1536-4c44-8ca2-1efc0f551dcf)


## Asinxron Funksiyalar (`async def`)

- `async` kalit so'zi funksiyani asinxron qilib belgilaydi. Bu funksiya ichida siz `await` kalit so'zidan foydalanib
  boshqa
  asinxron funksiyalarni chaqirishingiz mumkin.
  ```python
  import asyncio

    async def my_async_function():
        print("Started")
        await asyncio.sleep(1)
        print("Finished")
  ```

---

## Await Kalit So'zi

- `await` kalit so'zi asinxron funksiya ichida boshqa asinxron funksiyani chaqirayotganingizni bildiradi va bu
  operatsiya tugaguncha kutadi.
  ```python
  async def main():
    print("Before")
    await my_async_function()
    print("After")

  asyncio.run(main())
  ```
- Yuqoridagi misolda `await asyncio.sleep(1)` deb yozilgan, bu 1 soniya kutishni bildiradi. `await` kalit so'zi
  yordamida bu kutish vaqti boshqa operatsiyalarni bajarishga imkon beradi.

---

## Asinxron Funksiyalarni Boshqarish

- Asinxron funksiyalarni boshqarish uchun `asyncio` modulidan foydalaniladi. Eng ko'p ishlatiladigan usul
  bu `asyncio.run()`
  bo'lib, u asinxron funksiyani ishga tushiradi.
  ```python
  import asyncio

  async def my_async_function():
      print("Started")
      await asyncio.sleep(1)
      print("Finished")

  async def main():
      await my_async_function()

  asyncio.run(main())
  ```

---

## Bir Nechta Asinxron Funksiyalarni Parallel Ishlatish

- Asinxron funksiyalarni `parallel` ravishda ishlatish uchun `asyncio.gather()` yoki `asyncio.create_task()` dan
  foydalanish mumkin.
  ```python
  import asyncio

  async def function_1():
      await asyncio.sleep(2)
      print("Function 1 finished")

  async def function_2():
      await asyncio.sleep(1)
      print("Function 2 finished")

  async def main():
      task1 = asyncio.create_task(function_1())
      task2 = asyncio.create_task(function_2())
      await task1
      await task2

  asyncio.run(main())
  ```
- Yuqoridagi misolda `function_1` va `function_2` parallel ravishda ishga tushadi va kutilayotgan vaqtlari tugagach,
  natijalarini ko'rsatadi.

### Xulosa

- `async` va `await` kalit so'zlari asinxron dasturlashni osonlashtiradi va kutilayotgan kirish-chiqish operatsiyalari
  bilan samarali ishlashga imkon beradi. Bu texnologiyalarni to'g'ri qo'llash dastur performansini sezilarli darajada
  oshirishi mumkin.

#### © 2024 [themusharraf](https://github.com/themusharraf)
