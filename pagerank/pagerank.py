import os
import random
import re
import sys
import copy
import math

DAMPING = 0.85
SAMPLES = 20000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    
    transition = dict()
    
    #assgin initial ranks for each page in corpus
    for key in corpus:
        
        transition[key] = (1 - damping_factor) / len(corpus)
    
    #assign new ranks per page arguement
    for key in transition:
    
        if key == page:
        
            for eachpage in corpus[key]:
                transition[eachpage] = transition[eachpage] + (damping_factor / len(corpus[key]))
    return transition        
    


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    
    sample_dict = dict()
    markov_dict = dict()
    
    #initially assign sample ranks and markov ranks
    for key in corpus:
        sample_dict[key] = 1 / len(corpus)
        markov_dict[key] = float(0)
    
    
    for i in range(n):
        
        currpage = random.choices(list(sample_dict.keys()), weights=sample_dict.values(), k=1)
        pageStr = currpage[0]
        for key in markov_dict:
            if key == pageStr:
                #keep track of markov ranks per each page selection
                markov_dict[key] += 1 / n
        sample_dict = transition_model(corpus, pageStr, damping_factor)
    
    
    
    return markov_dict
        
    
    


def iterate_pagerank(corpus, damping_factor):
    
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    iter_ranks = dict()
    new_ranks = dict()
    
    d = damping_factor
    
    #initially assign ranks of iter_ranks and new_ranks(2 separeate dicts to keep track of converge )
    for key in corpus:
            iter_ranks[key] = 1 / len(corpus)
            new_ranks[key] = float(0)
            
    cycle = True
    
    while cycle:
        for page in iter_ranks:
            totalOfLinks = float(0)
            
            
            for poss_page in corpus:
                
                #calculate each link in each corpus page if it links to iter_ranks[page]
                if page in corpus[poss_page]:
                    totalOfLinks += iter_ranks[poss_page] / len(corpus[poss_page])
                    
                #calculate each link in each corpus page if it not links to iter_ranks[page]
                if not corpus[poss_page]:
                    totalOfLinks += iter_ranks[poss_page] / len(corpus)
            
            #applying the iterative pagerank formula to get new page rank
            new_ranks[page] = (1 - d) / len(corpus) + d * totalOfLinks
            
            cycle = False
            
            #check the converge for each pagerank and make the while loop continue if difference is not lowe than 0.001
            for page in iter_ranks:
                if not math.isclose(new_ranks[page], iter_ranks[page], abs_tol=0.001):
                    cycle = True
                    
                iter_ranks[page] = new_ranks[page]
                
    return iter_ranks
            
        
            
    
    
    

                
            
        
        
    
        
        
                    

        
    

if __name__ == "__main__":
    main()
