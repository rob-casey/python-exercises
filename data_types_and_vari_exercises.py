{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "695633ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "5. You have rented some movies for your kids:\n",
    "    \n",
    "    The Little Mermaid for 3 days\n",
    "    Brother Bear for 5 days\n",
    "    Hercules for 1 day\n",
    "    \n",
    "If the daily fee to rent a movie is 3 dollars, how much will you have to pay?    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "b63204e9",
   "metadata": {},
   "outputs": [],
   "source": [
    "## Create Variables\n",
    "the_little_mermaid = 3\n",
    "brother_bear = 5\n",
    "hercules = 1\n",
    "daily_fee = 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "60ebf204",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "27"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies = the_little_mermaid + brother_bear + hercules\n",
    "movies\n",
    "\n",
    "total_cost = movies * daily_fee\n",
    "total_cost"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e2b95650",
   "metadata": {},
   "outputs": [],
   "source": [
    "6. Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook.\n",
    "\n",
    "    They pay you the following hourly rates:\n",
    "\n",
    "    Google: 400 dollars\n",
    "    Amazon: 380 dollars\n",
    "    Facebook: 350 dollars\n",
    "        \n",
    "    This week you worked: 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.\n",
    "        \n",
    "    How much will you receive in payment for this week?    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "6d1e3cc0",
   "metadata": {},
   "outputs": [],
   "source": [
    "## Create Variables\n",
    "\n",
    "google = 400 * 6\n",
    "amazon = 380 * 4\n",
    "facebook = 350 * 10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "278cae60",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7420"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "payment = google + amazon + facebook\n",
    "payment"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ba6d14f4",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3621842811.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  Input \u001b[0;32mIn [1]\u001b[0;36m\u001b[0m\n\u001b[0;31m    7. A student can be enrolled to a class\u001b[0m\n\u001b[0m       ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "7. A student can be enrolled to a class only if the class is not full \n",
    "   and the class schedule does not conflict with her current schedule."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a8b2d94a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "class_not_full = True\n",
    "schedule_not_conflict = True\n",
    "enrolled_student = class_not_full and schedule_not_conflict\n",
    "enrolled_student"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ecd0a557",
   "metadata": {},
   "outputs": [],
   "source": [
    "8. A product offer can be applied only if people buys more than 2 items, \n",
    "   and the offer has not expired. \n",
    "   Premium members do not need to buy a specific amount of products."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "2b521b01",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "items_plus = True\n",
    "items_not = False\n",
    "offer_available = True\n",
    "offer_not = False\n",
    "premium = True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "0e4af19a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "product_offer = items_not and offer_not\n",
    "product_offer"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
