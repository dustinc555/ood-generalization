FROM continuumio/miniconda3:latest

WORKDIR /workspace

COPY environment.yml requirements.txt ./

RUN conda env create -f environment.yml

# Auto-activate environment
RUN echo "source /opt/conda/etc/profile.d/conda.sh && conda activate clinicaldg" >> /root/.bashrc

CMD ["bash", "--login"]
