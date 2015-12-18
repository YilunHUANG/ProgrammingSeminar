#A Brief Intoduction to Using Amazon Product Advertising API

---

##Mechanism
Request(URL) -> Amazon Server -> Response(XML)

##What we can do by using this API
* Get very detailed information of one product or a bunch of products from a certain category 
( Images, Reviews, SalesRanking, Similar products, etc. )
* Do some operations on shopping cart
* and some more things that I don't know yet

##Preparation

Three things we need to use the Amazon API:

* [Associate Tag](https://affiliate.amazon.co.jp/)
* [Access Key ID](https://affiliate.amazon.co.jp/gp/advertising/api/detail/main.html)
* [Secret Key ID](https://affiliate.amazon.co.jp/gp/advertising/api/detail/main.html)

Join the Amazon Associate Program to get your `Associate ID` (Associate Tag):
[https://affiliate.amazon.co.jp/](https://affiliate.amazon.co.jp/)

Register the Amazon Product Advertising API service to get your own `Access Key` and `Secret Key`:
[https://affiliate.amazon.co.jp/gp/advertising/api/detail/main.html](https://affiliate.amazon.co.jp/gp/advertising/api/detail/main.html)


##Send a request
Request Example:
```
http://ecs.amazonaws.com/onca/xml?
Service=AWSECommerceService
&Version=2011-08-01

&Operation=ItemSearch
&SearchIndex=Books
&Keywords=harry+potter

&Timestamp=
&AssociateTag=
&AWSAccessKeyId=
&Signature=
```

URL:
```
JP  http://ecs.amazonaws.jp/onca/xml
    https://aws.amazonaws.jp/onca/xml
US  http://ecs.amazonaws.com/onca/xml
    https://aws.amazonaws.com/onca/xml
```

Parameter:

 * Required
```
Service=AWSECommerceService

Operation=            what operation you want to do

Timestamp=            the current time 
AssociateTag=         your Associate ID
AWSAccessKeyId=       your Access Key
Signature=            need to be computed
```
Some **Operations** we often use:
`ItemLookup`: Search item by using ISBN or ASIN  
`ItemSearch`: Search item by keyword (SearchIndex, Title, Author, Publisher, Brand, Artist and so on..) 
`BrowseNodeLookup`: Get the detailed structure of one category
`CartCreate`, `CartAdd`


See more kinds of Operation and their required parameters: [Go to awsdocs](http://s3.amazonaws.com/awsdocs/Associates/latest/prod-adv-api-qrc.pdf)

Sample code for computing signature. [Go check it](https://aws.amazon.com/code/Product-Advertising-API)
And a great tool to help you understand the progress of computing signature: [Signed Requests Helper](https://associates-amazon.s3.amazonaws.com/signed-requests/helper/index.html)

* Optional
```
Version= 
MerchantId=           Default is Amazon, specify some Id or use All
ResponseGroup=        Which kind of information you want from Amazon
```

Some **ReponseGroup** we often use:
`Small`, `Medium`, `Large`, `Similarities`, `Reviews`, `Images`, `SalesRank`

##Receive a response(XML)
* Use tools to extract information from XML 
(It can be done by using any kinds of programing language, so I just skip here)


##Reference in Japanese
(Go check it)[http://www.ajaxtower.jp/ecs/]

 
