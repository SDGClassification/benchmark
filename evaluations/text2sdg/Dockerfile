FROM r-base:4.4.0

# Install dependencies
RUN apt update -y && apt install -y --no-install-recommends libxml2-dev

# Install text2sdg
RUN R -e "install.packages('text2sdg')"