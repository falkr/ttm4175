# Binary and IP Addresses

Last week you have already learned about IP addresses and how to connect your Raspberry Pi to the Internet.
Now you will learn even more about IP addressing and the fundamental aspects that enable the Internet.

To know more about networking we will be using the book [Computer Networking: A Top Down Approach](http://gaia.cs.umass.edu/kurose_ross/index.html), 7th edition.
We will be using this book in the upcoming three weeks and in the course TTM4200 in the Spring semester, so please try to get a copy as soon as possible.

:aside: If you get the 8th edition there's no problem, the main contents are similar.


Reading the *first chapter is recommended* but not mandatory.
Each week will focus on specific sections that need to be read and understood.
*Details about the required readings will be available every week, **in bold**.*

## Learning Goals

:goals: After this week you will be able to:

- Understand and apply basic binary arithmetic
- Understand IP addresses and their organisation into subnets
- Create and configure Local Area Networks (LANs)
- Use basic Linux commands for managing:
    - IP addresses (IPv4 and IPv6)
    - IP subnets and masks


# How do computers communicate?

## Introduction to binary

Binary code is fundamental in digital systems and computers.
This video will give several examples of how binary code is used and even touches on ternary and quantum possibilities...

---
type: youtube
video: wgbV6DLVezo
---

## Binary Numbers

IP numbers, which we briefly looked earlier, are represented by binary numbers.
However, this can sometimes be tricky to visualise.
The following videos will help you understand how you can convert a number from binary do decimal and vice-versa. 
This will be very useful when working with IP addresses and subnets.

---
type: youtube
video: SDG3exslzio
---

---
type: youtube
video: H4BstqvgBow
---



# Understanding IP addresses and subnets

The following video gives a short overview how IP addresses are used on our everyday lives whenever we use the Internet (watch the first 2min only).

---
type: youtube
video: 7_-qWlvQQtY
---
<!--_ -->

This video also introduces IP addresses in a slower but more complete way.

---
type: youtube
video: L6bDA5FK6gs
---


## More about IP addresses

Focusing on IP addresses, and to prepare for the lecture's quiz, you need to **read from section 1.1 to 1.2.1 of the book (from page 30 to page 39)**.
If you already read the first chapter you can check the additional materials below.

:aside: This will also be included in the RAT, don't ignore it!


## Setting up a second VM

In the upcoming networking labs\. we will use another VM, this time using the [Ubuntu](https://ubuntu.com/) Linux distro.

This VM is more complex and has additional software installed, which means you'll need more disk space to import it.
Please make sure you have **at least 20GB** of free disk space for working with this VM.

:tip:
This same virtual machine is going to be used in TTM4200, next semester. If you keep it you'll save some time later!

Another tip, my laptop is a bit old and has limited disk space. I use an external SSD disk drive to keep my VMs.


It's also important that you download the VM image [here](
https://filesender.uninett.no/?s=download&token=a0ca6d46-2078-4984-a532-b68e3fd2cbaf).

Finally, if you wish, you can start importing the downloaded image. The password is "ttm4200" (don't forget to change it!).


# Additional materials

The materials below won't be tested but will be very important in a near future.

## Routing

The videos and readings above already provided some insights about routing.
However the following video provides more information and shows the importance of routing in today's Internet.

---
type: youtube
video: AkxqkoxErRk
---

If you want to know some more about the Internet and network stacks the following video is also very interesting.

---
type: youtube
video: PG9oKZdFb7w
---


## Subnets

We will talk more about IP subnets in the classroom.
However, if you want to learn more about it in advance, you can check this video with a pizza analogy for subnets!

:aside: this one is a bit too slow but it motivates _why_ we want subnets.

---
type: youtube
video: -yz3FV8WliU
---

This second video on IP subnets is quite long but gives plenty of examples for those of you feeling curious about the arithmetic part.

---
type: youtube
video: XQ3T14SIlV4
---


## Delays and packet loss

Surely you've experienced "lag" and "loss of connection".
You can read more about these phenomena in pages 62--66 and 69--70.
Of course, if you've already read Chapter 1 you'll already know all about this!


## Virtual machines

By now you're already familiar with virtual machines.
However, if you still have questions about what a VM is, this short video can provide some help.

:aside: We don't endorse some of the language used in this video!


---
type: youtube
video: yIVXjl4SwVo
---


