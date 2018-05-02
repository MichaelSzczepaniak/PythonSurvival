### Survival Analysis Tools

Starting with a three column dataframe: Time2E, EventCount, and CensorCount, compute three additional columns:

+ AtRiskCount - count of at risk subjects
+ PropSurvInt - proportion surviving in interval Time2E(t) and Time2E(t-1)
+ ProbSurv - probablity of surviving up to Time2E

Works through [this example](https://www.youtube.com/watch?v=Wqg0wlQ1nTs) from Lori Wilbur's YouTube presentation