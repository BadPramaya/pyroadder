o
    <��br  �                   @   s~   d dl Z d dlmZmZ d dlZd dlZe�  ejZejZ	ej
ZejZejZejZejZejZe	eeeegZdd� Ze�  dS )�    N)�init�Forec                  C   s2  t dt� d�� zt�d�} W n   t t� d�� t t� d�� Y t| j�dkr�ttt� d| j� dt� ���}|d	ksD|d
ksD|dkrt t� d�� t	j
dkr[t	�d� t	�d� n
t	�d� t	�d� t	�d� t	�d� t t� d| j� �� td� d S t t� d�� td� d S t t� d�� td� d S )N�
z[i] Checking for updates...zDhttps://raw.githubusercontent.com/msy1717/pyroadder/main/version.txtz& You are not connected to the internetz) Please connect to the internet and retryg�������?z[~] Update available[Version z]. Download?[y/n]: �yZyes�Yz[i] Downloading updates...�ntzdel main.pyzdel setup.pyz
rm main.pyzrm setup.pyzLcurl -l -O https://raw.githubusercontent.com/msy1717/pyroadder/main/login.pyzLcurl -l -O https://raw.githubusercontent.com/msy1717/pyroadder/main/adder.pyz[*] Updated to version: zPress enter to exit...z[!] Update aborted.z Press enter to goto main menu...z%[i] Your script is already up to date)�print�lg�requests�get�r�float�text�str�input�os�name�system)�version�prompt� r   �&/storage/emulated/0/pyrogram/update.py�update   s.   





r   )r
   Zcoloramar   r   �time�sysZRESET�nZLIGHTGREEN_EXr	   ZLIGHTRED_EXr   ZWHITE�wZCYAN�cyZLIGHTYELLOW_EXZyeZLIGHTMAGENTA_EXZmgZLIGHTBLUE_EXZlbZcolorsr   r   r   r   r   �<module>   s     
