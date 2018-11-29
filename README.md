# insight

 Identifying a host with just an IP or domain name is nearly impossible. `insight` searches several online services for information about a host. It pulls service and location data from [Shodan](https://www.shodan.io/), certificate data from [Censys](https://censys.io/), and queries [GreyNoise](https://greynoise.io/) just to name a few.

## Background

Throughout my time running a [global network of honeypots](https://github.com/becksteadn/honeystash) I recorded thousands of IP addresses that had tried to log in to a computer I owned. If I was curious about one I'd search all of the above services individually and look at the documentation for correct syntax if I was searching something specific. This tool is made to be a starting point when investigating.

### Name

I started this project the day NASA's [InSight Mars Lander](https://mars.nasa.gov/insight/)  touched down on the red planet.

# Usage

I'm working on packaging, but in the mean time you can run it with these steps.

`git clone https://github.com/becksteadn/insight.git && cd insight`

`virtualenv .env`

`source .env/bin/activate`

`pip install -r requirements.txt`

`cd insight`

**Optional** Add your Censys and Shodan keys to `insight.yml`

`python insight.py [host]`