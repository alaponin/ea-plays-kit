# The anomaly rubric

An anomaly is an observation with numbers, a pattern name, and a question. It is never a
conclusion about a member's conduct and never about a citizen.

| Pattern | The numbers that evidence it | The question shape | Who answers (post) |
| --- | --- | --- | --- |
| rising failure rate | failure rate this period vs the previous, per service; the fault codes | *Did the provider change its interface on [date] (a contract drift — B24), or is the consumer retrying on a transient fault?* | the provider's technical contact; the Operating Authority |
| rising latency | median and p95 this period vs the previous | *Has load grown, or has the provider's forwarding target slowed? Is the SLA target (B30) breached?* | the provider's technical contact |
| volume spike | calls per hour or per day against the period's median | *Does a business event explain it — an exams window, an enrolment deadline — or is a client looping?* | the consumer's technical contact |
| new caller | a caller-service pair with no calls in the baseline period, or not in the ACL as B33 records it | *Was a grant added, and under which catalogue exchange and lawful basis? If no grant exists, why did the call not fail?* | the Operating Authority |
| off-hours surge | calls in the hours the member's services are not offered (B30 support hours) | *Is a batch job scheduled, or is a credential being used outside its purpose?* | the consumer's technical contact; the data-protection officer if it persists |
| run of access-denied faults | count of `AccessDenied` faults from one caller to one service | *Is the caller misconfigured, or is a consumer attempting a service it was refused? Either way, who at the caller knows?* | the caller's technical contact |
| service gone quiet | a service with calls in the baseline and none now | *Is the provider down, unregistered, or did the consumer stop needing it? Is a citizen being asked again at a counter?* | the provider's technical contact |
| size anomaly | response size far above the median for a service | *Is the service returning more fields than its contract declares (B33 assertion 5)?* | the provider's technical contact; the Technical Working Group |

## Ranking

1. anything that could mean a citizen is asked again, or receives a wrong answer
2. anything that could mean data is flowing without a grant, or beyond a contract
3. anything that breaches a member obligation or SLA
4. everything else

## The quarterly paragraph

Name the subsystems (not the people) with sustained failure or unusual behaviour; give the
numbers and the period; state the SLA target beside them where one exists; recommend a
conformance re-check where the pattern persisted across the quarter; and say what the logs
could not show.
