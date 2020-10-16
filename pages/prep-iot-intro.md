# Internet of Things

Most of you have heard about the *Internet of Things* or IoT in various settings, how it *"connects everything"* and makes *"everything smart"*. It's hard to tell which of the predictions will come true and which ones will remain fantasy. Some products are useful to some (I for example really like that my door does not need a physical key anymore), some products will remain useless, and maybe we haven't thought of the really useful applications yet.

In this week, we start by looking at some of the ingredients of IoT systems, some of the challenges, and start programming an IoT device in Python.

A good way of thinking about IoT is to understand the underlying technological trends that happened over the last decades: 

- **Embedded computing** devices get smaller, cheaper and more energy-efficient. This makes it feasible to embed computers into all kinds of devices. The term _embedded_ simply means that the computation is not happening in a general-purpose computer (like your laptop) but embedded into another system or product.
- **Mobile coverage** is improving, and new protocols are available that are suitable for energy-efficient machine-to-machine communication. 
- Advances in **data analytics** and machine learning make it possible to process data and learn from it, so that data gathered by many embedded devices can be transformed into valuable knowledge.

These trends make it possible that general things (and not only typical computers and phones) can gain computational power and be connected to the internet.
Examples are often grouped into different **domains**, many of them referring with the word "smart" to the fact that they are computational and communicating:

- **Smart Home**: Light bulbs can be controlled remotely, and the house can be instrumented with sensors to detect if someone is breaking in, water leaks or fire starts. It can also be used to measure temperature and humidity in each room for climate control.
- **Smart Buildings**: In larger buildings, heating and lights can be controlled according to where people are, and facilities such as toilets are cleaned in proportion with their usage.
- **Smart City**: Living conditions and usage patterns can be monitored, such as noise or air quality. Examples are also smarter handling of waste, as waste bins can tell how full they are and energy can be saved by not emptying bins that are not yet full.
- **Smart Grid**: This is the term for the energy distribution net, which to an increasing degree gets digitalized so that it can be monitored and controlled better.
- **Industry 4.0**: Tools and fabrication facilities can be better instrumented to have better control over the production process.
- **Precision Agriculture**: Soil moisture can be monitored and controlled in much more fine-grained levels so that water and fertilizer or fungicides can be applied much more targeted. Animals can be tracked and their behavior observed.
- **Intelligent Traffic Systems**: Monitoring the state of roads with regard to weather, and infrastructure like bridges and tunnels for structural safety.

These are just a few examples. Most of them have in common that they monitor some phenomena (like the physical properties of something) or observe resources so that we can make better decisions that, in the end, save valuable resources.
But apart from these potential benefits, there is also a long list of **challenges, problems and dangers** that come with this type of system. 

- **Privacy**: More devices around us that collect more data are also a challenge regarding privacy, when data is used differently than originally intended, unaware by who is observed, or simply stolen.
- **Security**: More connected devices mean a larger surface for attacks. This is dangerous for the devices or the connected systems, but also for other systems, as IoT devices can be used for distributed denial of service attacks that can render other systems unusable. 
- **Safety**: When cars or other potentially dangerous devices get connected, we need to focus on the implications for safety.
- **Electronic Waste**: We cannot just build more and more electronics with short lifecycle without worrying where the poisonous materials for their production come from or where they end up. Also note that the waste problem does not only mean what is happening with the specific device _after_ its lifetime, but that its production already created a lot of problematic waste _during its production_.




## IoT Security, Safety, Privacy

Let's first have a look at security in general in a video that also provides some context about IoT:

<!-- 15:15 -->

---
type: youtube
video: D3yrk4TaIQQ
---


## Safety in IoT

<!-- 7:48 -->

This is a video from the Computerphile Channel, where Ross Anderson explains the challenge with the Internet of things with regard to safety. 

---
type: youtube
video: PLiE0Nr8VOE
---

One of the main arguments in this video is that IoT creates a new category of device. Before, we had two types of devices:

* Devices with short lifetimes (2-5 years), like computers and mobile phones. During their short lifetimes, they receive monthly updates for security until they are replaced since there are much more powerful devices.
* Devices with long lifetimes (>10-20 years), like cars or fridges, which are engineered once, then tested but do not regularly receive updates. 

With the IoT, the division between these two categories is getting blurry: A device that should have a long lifetime (like a car or a fridge) is combined with a components that has a traditionally short lifecycle (the embedded computer), and suddenly a device may need critical security updates several decades into the future! 

---
type: figure
source: figures/iot/iot-lifetime.png
caption: "IoT devices combine functions that have very different lifetimes."
---

Think about the dilemma with these different life cycles. Is this a reason why a smart fridge is really a bad product idea? Here is a nice article: [Smart Fridges Are Still a Dumb Idea](https://www.ifixit.com/News/7747/smart-fridges-dumb-idea)



## Privacy in IoT

<!-- 17:37  -->

The following is an interview with [Richard Stallman](https://en.wikipedia.org/wiki/Richard_Stallman), the founder of the Free Software Foundation. The interview starts a bit awkward, but gets into the fundamental privacy issues raised by IoT. 

---
type: youtube
video: AAP4N3KyLmM
---


## Electronic Waste


Electronic waste in a general problem, but it has implications on what we need to consider when we want to understand the impact and challenges with the Internet of Things:
 
- On the one side, the IoT devices itself are electronic devices that contribute to waste. As said above, even if devices are small and cheap, we cannot just keep producing them without considering their entire life cycle.
- On the other side, making devices like fridges that traditionally had a long life span into electronic devices can give them a much shorter life span, and by that indirectly contribute to the problem of electronic waste. 

The video below is a longer one, and viewing it is optional. But have a look at it, just to get an impression of how severe this problem is.

---
type: youtube
video: QTU1F865JJo
---