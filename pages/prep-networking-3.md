# NAT and Wi-Fi

At this point, understanding addressing, routing and how to dynamically handle hosts, we can now create our own private network.
Since a network disconnected from the Internet may not be so interesting you will now learn how one public IP address can be used by several hosts, using IP Masquerading, typically referred to as Network Address Translation (NAT).
In addition, since the IEEE 802.11 wireless protocol, or Wi-Fi, is so commonly used for connectivity, you will also learn how to create your own Wi-Fi access point using a Raspberry Pi.

This week's readings will still be based on the book [An Introduction To Computer Networks](http://intronetworks.cs.luc.edu/).
Remember that the *details about the required readings will be available in each section, **in bold**.*

## Learning Goals

:goals: After this week you will be able to:

- Understand how IP Masquerading/NAT works
- Understand how Wi-Fi works
- Use basic Linux commands for:
    - configuring IP masquerading
    - installing and configuring a basic Wi-Fi access point


# Understanding NAT

As you now know there are special types of IP addresses and a lack of public IPv4 addresses.
Network Address Translation (NAT) allows us to minimise this issue through IP Masquerading and a lot more (e.g. improve security).
To learn more about NAT read **section 7.7 and its subsections (from page 200 to 204)**.
In addition, you may also read more IP Masquerading in Linux [here](http://www.tldp.org/HOWTO/IP-Masquerade-HOWTO/ipmasq-background2.0.html).
Wikipedia is also an interesting resource for knowing more about [NAT](https://en.wikipedia.org/wiki/Network_address_translation).


# Understanding Wi-Fi

Wi-Fi is nowadays present in almost every household, office, public transport, \ldots 
We use it in our computers, phones, smart-watches, TVs, consoles, …
But how does it work?
Read more about it in:

- **section 3.1.7 (pages 99 and 100)** and
- **sections 3.7.4 and 3.7.4.1 (from page 107 and 110)**.

