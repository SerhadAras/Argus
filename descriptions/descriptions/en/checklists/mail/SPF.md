# Mailchecks - SPF

## What is SPF?

When receiving an email, how certain are we that its original sender really is the stated sender?
the answer on that question is: if there is no SPF set, we don't know.

SPF, Sender Policy Framework is an email authentication method. With SPF, the owner of a domain is able to define which IP addresses are allowed to send emails for its specific domains.
The receiver will automatically check whether the mail was sent from the IP addresses specified in the SPF.


## Why do I need SPF?

By using SPF, the domain owners gain the ability to protect their domain from unauthorized use, also known as "email spoofing".
Without properly defining the IP addresses, attackers can easily send phishing emails and email scams as if they came from your domain.


## Source

[Wikipedia - Sender policy framework](https://en.wikipedia.org/wiki/Sender_Policy_Framework)

[SparkPost - Understanding SPF and DKIM to improve email deliverability](https://www.sparkpost.com/blog/understanding-spf-and-dkim/)
