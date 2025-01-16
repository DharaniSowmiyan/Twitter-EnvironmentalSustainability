SOCIAL MEDIA DATA ANALYSIS ON ENVIRONMENTAL SUSTAINABILITY 
=

ABSTRACT:
=
Social media data plays a significant role in understanding the society’s perspective of a particular situation. Social media platforms such as twitter enables users to post their unfiltered opinions in the form of tweets. These tweets can be used as a powerful tool to understand people’s point of view in the domain of our interests such as environmental sustainability. Our project focuses on analysing twitter users tweets based on topics related to environmental sustainability and analyse the public sentiments. In this we’ve performed sentimental analysis on the tweets using BERT model and based on those sentiment labels we have performed various analysis measures to uncover new levels of detail about human-environment interactions. This report focuses on the opportunities , threats and challenges associated with the use of social media data in sustainability.


INTRODUCTION:
=
The integration of social media data into environmental sustainability research presents significant opportunities and challenges. Social media platforms such as Twitter, Facebook, and Instagram represent volumes of data that are increasingly integral to research into environmental sustainability. By analysing this data, researchers uncover new levels of detail about human-environment interactions, track changes, and engage the public in sustainability issues. This report summarizes the key themes identified from this critical review which emphasis on both opportunities and challenges associated with the use of social media data in sustainability.


OPPORTUNITIES:
=
Social media data offer a unique insight into public opinion and behaviour about the environment. Using such data, researchers can track how people discuss climate change, renewable energy, and other sustainability issues. This information can help assessing the impact of environmental policies, and understand how people respond to natural disasters.
1.Understanding Human-Nature Interactions:  The knowledge from this data is crucial in showing behavioural patterns, public perception about environmental policies, and responses towards natural hazards.

2. Real-Time Monitoring: The real-time nature of social media communication enables continuous monitoring of environmental changes and social responses. This is particularly useful in disaster risk reduction, where timely data can inform rapid responses to events like floods, wildfires, and hurricanes.
3. Public Engagement and Awareness: Social media is one of the most influential tools for increasing awareness and engaging the public on environmental issues. By analysing social media content, researchers can measure public sentiment, track the spread of sustainability messages, and understand the dynamics involved.

THREATS AND ETHICS:
=
However, there are many issues with using social media data. Most often, the data available to researchers is restricted by the social media companies themselves, making it difficult to gather deep longitudinal data. Then, there are ethical issues concerning user privacy and ensuring that data is used in a manner that is responsible. In addition, social media data may be biased since it may not depict all demographic groups in equal measure. 
1.Data Accessibility: Social media platforms control access to their data, and they can change their rules, limit access, or even shut down. This makes it hard for researchers who need stable, long-term data access. 
2.Ethical Concerns: Using social media data comes with ethical challenges. Researchers need to be careful about privacy, getting user consent, and keeping data secure. The Cambridge Analytica scandal showed how important it is to follow strict ethical guidelines.
 3.Data Biases: Social media data can be biased because it reflects the demographics of users, how platforms prioritize content, and what users choose to share. These biases can affect research results, making them less representative of different regions or groups of people.

DATASET COLLECTION:
=
We’ve collected the tweets based on sustainability by a web scrapping tool called Bardeen.ai by specifying the keywords such as disasters, sustainability development, climatic changes that we would want to extract from the tweets.
The features of our dataset include:
 Name: The name of the Twitter user.
Handle: The Twitter username or handle of the user.
Media URL: Link to any media (images, videos) included in the tweet.
Retweets: Count of retweets received by the tweet.
Likes: Count of likes received by the tweet.
Comments: Count of comments or replies to the tweet.
Views: Count of views the tweet has received.
Tweet URL: Link to the original tweet.
Profile Link: Link to the user’s profile.
Post Body: The full, original text content of the tweet.
Date: Date when the tweet was posted.
Timestamp: Exact time when the tweet was posted.

TWEET PRE-PROCESSING:
=
Since the tweets may be in different formats such as the case, special characters and non-english characters we need to bring the tweets to a standaradized format. In-order to do sentimental analysis, the model understands the tweets only if it is the standard format we’ve used text pre-processing library known as NLTK which was used for performing tokenization and lemmatisation, it includes a new feature cleaned post body.
Cleaned Post Body: Processed and cleaned version of the tweet’s text, for sentiment analysis.


SENTIMENTAL ANALYSIS:
=
The sentiments of the tweets were analysed to categorize it into two labels: positive and negative. We tested three models and chose the model which gave the highest accuracy.
bert-base-uncased accuracy: 0.9444
roberta-base accuracy: 0.9444
distilbert-base-uncased-finetuned-sst-2-english accuracy: 0.6889

Best model: bert-base-uncased with accuracy 0.9444
Since the BERT model gave the highest accuracy it was chosen to label the tweets based on their sentiments, which provided the inclusion of a new feature sentiments.
Sentiment: Sentiment label (e.g., positive or negative) assigned to the tweet content for analysis.


DATA PRE-PROCESSING:
=
The data should be cleansed before processing. For that we formatted the data based on the date and handled missing value if it existed for categorical features we’ve replaced by using mode and for continuous features we’ve replaced by using it’s mean.


DATA SIMULATION:
=
Since the above features cannot be represented as a graph with nodes and edges as there is no relationship to be considered for drawing an edge. We’ve simulated three more features based on the values of the existing features.
followers_count: The number of followers the Twitter user has, indicating their reach and influence. It is based on retweets count.
retweeted_by: A list or count of specific users who retweeted the tweet, showing engagement from particular accounts.
mutual_friends: Users who are followed by both the tweet’s author and other specified users, helping to identify shared connections in the network.



VISUALIZATIONS WITH INFERENCE:
=
 Distribution of Followers Count
 

User handles who's Follower's count in the range of 5000-9.99k are more prominent. Influencers who have the followers count of more than 100k are less. Micro-influencers such as people with more than 5000-9.9k can also make a significant impact in influencing their followers.
Sentimental Analysis
 
People posting negative tweets about the environmental management beats positive tweets.
Engagement Metrics Over Time
 
Tweets during the time of Aug 2023- Oct 2023 received more likes, comments and retweets.
Retweets by Sentiment
 
 
On average, 121 retweets are tweeted for negative tweets and 151 retweets have been tweeted for positive.
Top 10 Tweets by Likes
 
 Relationship Between Followers and Engagement
 
Since in twitter,people retweet tend to retweet more if the person is popular with more follower's count the follower's count an retweet have a positive linear relationship .But only for people with 0-20k followers it is more influential.
Average Engagement by Sentiment
 
The positive tweets recieve more likes, retweets and comments eventhough the negative tweets are more.
Most Active Users
 
UNEP has tweeted the most with a total count of 32.
Bipartite Graph: Handles and Sentiment Labels
 
Sentiment Frequency:
sentiment
NEGATIVE    131
POSITIVE     50
Name: count, dtype: int64
Most Prominent Sentiment: 'NEGATIVE' with 131 occurrences.

Users connected to multiple sentiment labels:
               User  Connected   Sentiments
0     @robinmonotti  {NEGATIVE, POSITIVE}
1             @UNEP  {NEGATIVE, POSITIVE}
2           @UNFCCC  {NEGATIVE, POSITIVE}
3    @shellenberger  {NEGATIVE, POSITIVE}
4     @vanessa_vash  {NEGATIVE, POSITIVE}
5      @PaulEDawson  {NEGATIVE, POSITIVE}
6        @1_Akriti_  {NEGATIVE, POSITIVE}
7       @NatureDeal  {NEGATIVE, POSITIVE}
8               @UN  {NEGATIVE, POSITIVE}
9  @santhosh_reddy2  {NEGATIVE, POSITIVE}

Retweet Graph: Retweeting Users to Original Authors
 
Number of Nodes: 90
Number of Edges: 160
Density: 0.0200
Is the graph strongly connected? No
Is the graph weakly connected? Yes
Number of strongly connected components: 53
DEGREE CENTRALITY:
Most Influential Handle: @UNEP
In-Degree Centrality: 0.2809
UNEP has been frequently retweeted
CLOSENESS CENTRALITY:
Most Influential Handle by Closeness Centrality: @UNEP
Closeness Centrality: 0.3160
UNEP rapidly spread information or retweet content to a wider audience with minimal intermediaries.
BETWEENNESS CENTRALITY:
Most Influential Handle by Betweenness Centrality: @NatureDeal
Betweenness Centrality: 0.2581
NatureDeal controls information flow
EIGEN-VECTOR CENTRALITY:
Most Influential Handle by Eigenvector Centrality: @UNEP
Eigenvector Centrality: 0.5742
UNEP has not only widely retweeted but are also connected to other high-profile users, which amplifies their influence further
PAGE RANK:
Most Influential Handle by PageRank: @UNEP
PageRank: 0.1009
UNEP is likely a central figure, frequently connected
HUBS AND AUTHORITIES SCORE:
Top 5 Hubs:
@NatureDeal: 0.0876765982108818
@UNEP: 0.050686784452573144
@UN: 0.04814430768677097
@PaulEDawson: 0.0411138253406461
@Noahpinion: 0.039144711764382584


Top 5 Authorities:
@UNEP: 0.1476390747370618
@NatureDeal: 0.0629225348257271
@UN: 0.03457381086694184
@UNFCCC: 0.03268974776467032
@shellenberger: 0.030931147334965183

LOCAL CLUSTERING COEFFICIENT:
Average Clustering Coefficient: 0.2544
if User A frequently retweets User B, and many of User A's other followers also follow or interact with User B, it implies a strong interconnected community around User B's content.

GLOBAL CLUSTERING COEFFICIENT:
Global Clustering Coefficient (Transitivity): 0.05860
A high global clustering coefficient would indicate that many users in the network are involved in tightly-knit groups or communities where users frequently retweet each other's content.

BRIDGE NODES:
Bridge Nodes: ['@CrafteeThe', '@AlexEpstein', '@shellenberger', '@jasonhickel', '@SimoneFilippini', '@acecloula', '@LossandDamage', '@UN', '@vanessa_vash', '@CongressmanRaja', '@ECOWARRIORSS', '@TeahCartel', '@gummibear737', '@sanwatforall', '@_waleedshahid', '@RepJamesClyburn', '@UNFCCC', '@NatureDeal', '@thesangyan', '@jessesingal', '@UNEP', '@ClimateBen']
In the undirected version of the directed retweet graph, bridge nodes are crucial for maintaining the connectivity and flow of information between different communities.
COMMUNITY DETECTION:
GIRVAN-NEWMAN:
 
Community 1: ['@IISD_Energy', '@santhosh_reddy2', '@nature_org', '@georgefwoods', '@MonariPeterJ', '@PaulEDawson', '@rianphin', '@_waleedshahid', '@CNN', '@SDG16Plus', '@1_Akriti_', '@ClimateBen', '@Trad_West_Art', '@JamesMelville', '@IPBES', '@EarthKikashi', '@ChuckDalldorf', '@FredIutzi', '@Noahpinion', '@Ros_Rodriguez_', '@AirSupportBox', '@geoworldmedia', '@MrSolo4Dolo', '@WWF', '@weatherindia', '@JunkScience', '@EnergyBoom', '@AlokSharma_RDG', '@DrJenGunter', '@wtpBLUE', '@Rainmaker1973', '@DrJillStein', '@vanessa_vash', '@YOUTHBIODI51911', '@UN', '@UNClimateSummit', '@QuentinDempster', '@susantananda3', '@MichaelEMann', '@forumdc', '@zalisteggall', '@carddy_1', '@thesangyan', '@NatureDeal', '@AbiluTangwa', '@ECOWARRIORSS', '@shellenberger', '@grinnaija', '@Muskan_nnn', '@UntoThislast2', '@UNDRR', '@sanwatforall', '@PeterCorless', '@ATC_SPACES', '@MarkRuffalo', '@AlexEpstein', '@UNFCCC', '@jessesingal', '@EmilDimanchev', '@swaminathankp', '@ShahraDinesh', '@cwejournal', '@RoKhanna', '@tsuna_jj', '@SamLMontano', '@GuyCarpenter', '@KHayhoe', '@ChrisMartzWX', '@CrafteeThe', '@RepJamesClyburn', '@ClimateComms', '@TeahCartel', '@paraschopra', '@Tim_Canova', '@WriteEditPJ', '@houmanhemmati', '@CongressmanRaja', '@UNDP', '@gummibear737', '@keewa', '@NatureEcoEvo', '@robinmonotti', '@UNEP', '@GreenFlorence', '@UNBiodiversity']
Community 2: ['@acecloula', '@SimoneFilippini', '@ODPM_TT', '@LossandDamage', '@jasonhickel']

LOUVAIN ALGORITHM:
 
partition:{'@1_Akriti_': 0, '@robinmonotti': 0, '@CrafteeThe': 0, '@PaulEDawson': 1, '@UNEP': 0, '@NatureDeal': 2, '@UNFCCC': 3, '@AlexEpstein': 3, '@geoworldmedia': 0, '@shellenberger': 4, '@houmanhemmati': 0, '@CongressmanRaja': 5, '@UN': 6, '@LossandDamage': 6, '@RepJamesClyburn': 4, '@JamesMelville': 8, '@georgefwoods': 8, '@vanessa_vash': 6, '@grinnaija': 5, '@sanwatforall': 5, '@ATC_SPACES': 0, '@YOUTHBIODI51911': 5, '@JunkScience': 6, '@ChrisMartzWX': 1, '@SamLMontano': 3, '@jasonhickel': 6, '@ODPM_TT': 6, '@wtpBLUE': 0, '@Muskan_nnn': 4, '@ClimateComms': 2, '@cwejournal': 2, '@SimoneFilippini': 6, '@AirSupportBox': 6, '@GuyCarpenter': 6, '@RoKhanna': 5, '@_waleedshahid': 6, '@CNN': 6, '@DrJenGunter': 1, '@forumdc': 1, '@ClimateBen': 0, '@MichaelEMann': 0, '@TeahCartel': 1, '@ChuckDalldorf': 0, '@ShahraDinesh': 1, '@AbiluTangwa': 7, '@jessesingal': 2, '@QuentinDempster': 2, '@PeterCorless': 7, '@thesangyan': 7, '@WWF': 3, '@rianphin': 0, '@Rainmaker1973': 3, '@gummibear737': 5, '@ECOWARRIORSS': 8, '@Trad_West_Art': 8, '@NatureEcoEvo': 0, '@IPBES': 2, '@susantananda3': 3, '@nature_org': 0, '@MarkRuffalo': 2, '@paraschopra': 4, '@Noahpinion': 8, '@santhosh_reddy2': 6, '@EmilDimanchev': 0, '@acecloula': 6, '@MrSolo4Dolo': 2, '@keewa': 6, '@FredIutzi': 3, '@MonariPeterJ': 2, '@Ros_Rodriguez_': 2, '@EnergyBoom': 2, '@KHayhoe': 0, '@WriteEditPJ': 3, '@DrJillStein': 2, '@GreenFlorence': 6, '@swaminathankp': 1, '@carddy_1': 2, '@EarthKikashi': 2, '@tsuna_jj': 0, '@AlokSharma_RDG': 4, '@Tim_Canova': 5, '@UNClimateSummit': 4, '@UntoThislast2': 7, '@IISD_Energy': 5, '@UNDP': 1, '@SDG16Plus': 7, '@UNDRR': 4, '@UNBiodiversity': 2, '@zalisteggall': 5, '@weatherindia': 2}
Modularity: 0.46493333333333337
Mutual Friends Network Graph
 
Number of Nodes: 90
Number of Edges: 143
Density: 0.0357
Is the graph connected? Yes
CENTRALITY MEASURES:
Top User by Degree Centrality: UN Environment Programme, Score: 0.4045
Top User by Closeness Centrality: UN Environment Programme, Score: 0.5705
Top User by Betweenness Centrality: UN Environment Programme, Score: 0.5354
Top User by Eigenvector Centrality: UN Environment Programme, Score: 0.5162
Here UNEP seems to be the most influential node based on all of the centralities, which means it is a friend to most of the nodes.

TRIADIC CLOSURE:
Triadic Closure Ratio: 0.0263
If two users have a common friend then how likely it is for the users to be friends. Here the triadic closure ratio is low indicating less possibility.

HOMOPHILY:
Homophily Ratio based on Sentiment: 0.7203
how often people who share the same sentiments are connected.

AVERAGE CLUSTERING COEFFICIENT:
Average Clustering Coefficient: 0.2128
Indicates the likelihood that the user's friends are also friends with each other.

GLOBAL CLUSTERING COEFFICIENT:
Global Clustering Coefficient (Transitivity): 0.07505
Indicates the general trend of mutual friendships among users.

AVERAGE PATH LENGTH:
Average Path Length: 2.9765
How accessible one user is to others.


COMMUNITY DETECTION:
GIRVAN-NEWMAN:
 
Community 1: ['TheCrafteeKitty', 'Pathfinders', 'Houman David Hemmati, MD, PhD', 'The Aureus Press', 'Jason Hickel', 'CNN', 'Fred Iutzi', 'ODPM Trinidad and Tobago', 'IISD Energy', 'Steve Milloy', 'UNCS News', 'Loss and Damage Collaboration (L&DC)', 'yussif', 'UN Environment Programme', 'UNDRR', 'Congressman Raja Krishnamoorthi', 'Gummi', 'Jesse Singal', 'MrSolo4Dolo', 'GO GREEN', 'Michael Shellenberger', 'James E. Clyburn', 'thatadult', 'Teach Cartel', 'Intriguing and unexpected content!', 'WWF', 'Rosmel RodrÃ\xadguez', 'Vanessa Nakate', "Tangwa Abilu..SDG's.", 'UN Development', 'UN Biodiversity', 'Natsu', 'Susan Joy Hassol, Climate Communication', 'Quentin Dempster', 'keewa', 'Dr. Samantha Montano', 'Noah Smith', 'Zali Steggall MP', 'Editorial office D+C', 'Paras Chopra', 'Rt Hon Lord Alok Sharma', 'ipbes', 'United Nations', 'ATC Spaces', 'Akritii', 'we the people (#wtpBLUE)', 'Emil Dimanchev', 'Tim Canova', 'Current World Environment', 'Robin Monotti', 'Geospatial World', 'NatureEcoEvo', 'Unto This Last', 'Society Groom', 'The Weather Channel India', 'Dr. Jill Stein', 'Peter Corless', 'Chris Martz', 'The Nature Conservancy', 'Prof Michael E. Mann', 'Alex Epstein', 'Florence Micoud', 'Jennifer Gunter', 'Simone Filippini', 'santhosh reddy', 'Prof. Katharine Hayhoe', 'YOUTH BIODIVERSITY CONSERVATION INITIATIVE -', 'Air Support Project', 'James Melville', 'Mark Ruffalo', 'EnergyBoom', 'Monari, Peter Joseph Ph.D', 'Muskan', 'UN Climate Change', 'Waleed Shahid', 'one earth(minoru .T)', 'Susanta Nanda', 'Nature Positive', 'Chuck Dalldorf', 'The Sangyan By Abhishek', 'Guy Carpenter', 'Dr. Dinesh Shahra', 'Paul Dawson', 'Massimo', 'Ro Khanna', 'Ben See']
Community 2: ['Georgina Woods', 'Sanitation and Water for All', 'Picpus', 'Swaminathan Padmanabhan']
LOUVAIN ALGORITHM
 
partition:{'Robin Monotti': 0, "Tangwa Abilu..SDG's.": 0, 'Nature Positive': 1, 'UN Environment Programme': 4, 'UN Climate Change': 3, 'Jennifer Gunter': 3, 'Alex Epstein': 5, 'Susan Joy Hassol, Climate Communication': 5, 'Michael Shellenberger': 4, 'Zali Steggall MP': 4, 'Houman David Hemmati, MD, PhD': 4, 'Vanessa Nakate': 4, 'ATC Spaces': 3, 'Loss and Damage Collaboration (L&DC)': 3, 'Dr. Jill Stein': 3, 'United Nations': 5, 'Georgina Woods': 5, 'Sanitation and Water for All': 5, 'Editorial office D+C': 1, 'YOUTH BIODIVERSITY CONSERVATION INITIATIVE -': 3, 'Massimo': 3, 'Chris Martz': 1, 'Paul Dawson': 0, 'Peter Corless': 3, 'ODPM Trinidad and Tobago': 3, 'Muskan': 3, 'Fred Iutzi': 5, 'Current World Environment': 2, 'Akritii': 2, 'Jason Hickel': 1, 'The Weather Channel India': 1, 'Air Support Project': 4, 'Picpus': 5, 'Guy Carpenter': 5, 'Ro Khanna': 4, 'Congressman Raja Krishnamoorthi': 3, 'James E. Clyburn': 1, 'Simone Filippini': 1, 'CNN': 1, 'Steve Milloy': 1, 'Natsu': 1, 'GO GREEN': 5, 'Chuck Dalldorf': 4, 'Prof Michael E. Mann': 4, 'Geospatial World': 0, 'Ben See': 4, 'Teach Cartel': 1, 'Quentin Dempster': 3, 'Dr. Samantha Montano': 1, 'The Sangyan By Abhishek': 4, 'we the people (#wtpBLUE)': 3, 'WWF': 1, 'thatadult': 2, 'Gummi': 4, 'The Aureus Press': 1, 'NatureEcoEvo': 5, 'yussif': 5, 'ipbes': 4, 'Susanta Nanda': 5, 'The Nature Conservancy': 5, 'Tim Canova': 2, 'Paras Chopra': 1, 'Mark Ruffalo': 1, 'Noah Smith': 2, 'Emil Dimanchev': 4, 'James Melville': 4, 'Jesse Singal': 5, 'Swaminathan Padmanabhan': 5, 'Dr. Dinesh Shahra': 2, 'UNDRR': 2, 'MrSolo4Dolo': 5, 'santhosh reddy': 5, 'keewa': 1, 'Rosmel RodrÃ\xadguez': 0, 'Rt Hon Lord Alok Sharma': 0, 'Society Groom': 3, 'Pathfinders': 1, 'Prof. Katharine Hayhoe': 4, 'UN Development': 3, 'Florence Micoud': 4, 'EnergyBoom': 1, 'TheCrafteeKitty': 3, 'Monari, Peter Joseph Ph.D': 2, 'one earth(minoru .T)': 4, 'Unto This Last': 1, 'IISD Energy': 5, 'Waleed Shahid': 4, 'UNCS News': 4, 'UN Biodiversity': 5, 'Intriguing and unexpected content!': 2}
Modularity: 0.4882634847669812

K-MEANS CLUSTERING:

 
Community 1: ['Robin Monotti', 'Robin Monotti', 'UN Environment Programme', 'UN Climate Change', 'Geospatial World', 'Michael Shellenberger', 'Houman David Hemmati, MD, PhD', 'UN Climate Change', 'UN Climate Change', 'Loss and Damage Collaboration (L&DC)', 'Alex Epstein', 'Georgina Woods', 'UN Environment Programme', 'Vanessa Nakate', 'YOUTH BIODIVERSITY CONSERVATION INITIATIVE -', 'Chris Martz', 'UN Climate Change', 'ODPM Trinidad and Tobago', 'UN Environment Programme', 'Muskan', 'Susan Joy Hassol, Climate Communication', 'Current World Environment', 'Jason Hickel', 'Air Support Project', 'Sanitation and Water for All', 'Guy Carpenter', 'Akritii', 'Ro Khanna', 'Congressman Raja Krishnamoorthi', 'James E. Clyburn', 'Editorial office D+C', 'Steve Milloy', 'Prof Michael E. Mann', 'Editorial office D+C', 'Paul Dawson', 'Chuck Dalldorf', 'Paul Dawson', 'Ben See', 'Teach Cartel', 'Quentin Dempster', 'Dr. Samantha Montano', "Tangwa Abilu..SDG's.", 'The Sangyan By Abhishek', 'Peter Corless', 'WWF', 'Nature Positive', 'Nature Positive', 'thatadult', 'Nature Positive', 'Massimo', 'Gummi', 'The Aureus Press', 'GO GREEN', 'NatureEcoEvo', 'ipbes', 'Susanta Nanda', 'The Nature Conservancy', 'Nature Positive', 'Nature Positive', 'Nature Positive', 'Nature Positive', 'Paras Chopra', 'Nature Positive', 'Nature Positive', 'Nature Positive', 'Noah Smith', 'Nature Positive', 'Emil Dimanchev', 'Nature Positive', 'Nature Positive', 'Nature Positive', 'UN Environment Programme', 'Jesse Singal', 'Jennifer Gunter', 'Nature Positive', 'Nature Positive', 'Picpus', 'Dr. Dinesh Shahra', 'MrSolo4Dolo', 'keewa', 'Fred Iutzi', 'Michael Shellenberger', 'Nature Positive', 'Nature Positive']
Community 2: ['Alex Epstein']
Community 0: ['Sanitation and Water for All', 'Paul Dawson', 'CNN', 'Paul Dawson', 'Nature Positive']
LOUVAIN USING GEPHI:

 

APPLICATIONS:
Despite these challenges, data from social media have been used in various ways to support the cause of environmental sustainability. Examples include monitoring public sentiment on climate change, assessment of biodiversity, and evaluation of the effectiveness of initiatives for sustainability. Once ethical issues are addressed and it is ensured that research will be conducted in a transparent manner, this data can be put into better use.
CONCLUSION:
=
Social media data hold significant promise for enhancing environmental sustainability research by providing real-time insights and broadening public engagement. However, realizing this potential requires careful consideration of ethical standards, data privacy, and accessibility issues. By addressing these challenges, researchers can ensure that social media data contribute positively to the global sustainability agenda, supporting efforts to achieve the United Nations Sustainable Development Goals (SDGs) and promoting a more sustainable future.

ATTATCHMENTS:
=
SENTIMENTAL ANALYSIS :
https://colab.research.google.com/drive/1bTFq707hcG-GzKUO9XzS__EaSa9ZGezG?usp=sharing
DATA FORMATTING:
https://colab.research.google.com/drive/1GgkSqeApzvQv1FVPSDjIA1rVYItyF0ru?usp=sharing
VISUALIZATIONS AND INFERENCE:
https://colab.research.google.com/drive/1GydmylrulXDlsy9dCOL55HqkUGZGmjlh?usp=sharing
COMMUNITY DETECTION USING GIRVAN NEWMAN AND LOUVAIN:
https://colab.research.google.com/drive/15s-S09KQXE_lQzZp_QmhlFNSMPA3RErR?usp=sharing
















