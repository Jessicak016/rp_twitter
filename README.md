### Relapsing Polychondritis in Twitter

This project is about analyzing tweet data to study conversations around relapsing polychondritis on social media. Relapsing polychondritis (RP) is a rare condition where there is not much discussion and awareness about its management, treatment and diagnosis. I used topic modeling method LDA and conducted network analyses to explore latent topics surrounding relapsing polychondritis in the tweets. This results showed that many of the tweets were focused on advocacy and raising awareness.

#### Files
- Data_Analysis_gensim.ipynb shows EDA, Topic Modeling with LDA and Network Analysis. 
- import_data.py imports tweet data using Twitter API. 
- process_tweets.ipynb processes imported tweets into usable formats. It exports tweets.csv, which is also included here. 
- get_users_data.py imports users who have retweeted those tweets.
- m3inference folder with the output files for [m3inference](https://github.com/euagendas/m3inference) module

#### Preparation
The code requires pandas, gensim, PIL, scikit-learn and networkx to run. 
It is recommended to use [Gephi](https://gephi.org/) software over networkx for visualizing user networks. 

More details about the project can be found in this blog post [here](https://jessjkim-1.medium.com/relapsing-polychondritis-in-twitter-cdfdb8b9f5a3?source=friends_link&sk=976e94e34af6222afad5ce3ff730bfa5). 

#### References
Isabel Anger and Christian Kittl. Measuring influence on twitter. InProceedings of the 11th International Conference on Knowledge Management and Knowledge Technologies, volume 31, pages 1–4, 2015.

Salvatore Pirri, Valentina. Lorenzoni, Gianni Andreozzi, Mosca Marta, and Giuseppe Turchetti. Topic modeling and user network analysis on twitter during world lupus awareness day. International Journal of Environmental Research and Public Health 2020, 17(5440), 2020.

Selva Prabhakaran. Topic modeling with gensim (python), 2018. Last accessed 20 Nov 2021.

Zijian Wang, Scott Hale, David Ifeoluwa Adelani, Przemyslaw Grabowicz, Timo Hartman, Fabian Flock, and David Jurgens. Demographic inference and representative population estimates from multilingual so-cial media data. In The World Wide Web Conference, pages 2056–2067.ACM, 2019.

Jia Xue, Junxiang Chen, Chen Chen, Chengda Zheng, Sijia Li, andTingshao Zhu. Public discourse and sentiment during the covid 19 pandemic: Using latent dirichlet allocation for topic modeling on twitter. PLos ONE, 15(9), 2020.


