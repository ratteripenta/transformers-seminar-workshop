import matplotlib.pyplot as plt
import seaborn as sns
import torch

sns.set()


def visualize_self_attention(
    x: torch.Tensor,
    raw_weights: torch.Tensor,
    weights: torch.Tensor,
    y: torch.Tensor,
    q: torch.Tensor = None,
    k: torch.Tensor = None,
    v: torch.Tensor = None,
):
    """
    Visualize the self-attention mechanism for each token in the sequence using heatmaps with annotations. 
    
    To do this, provide heatmaps with annotations for input embeddings, raw and scaled attention weights, and output embeddings after applying self-attention. If query, key, and value weight vectors used in the attention mechanism are provided, visualize them as well. To do this, provide the q, k, and v arguments with the corresponding weight vectors, and the function will generate heatmaps with annotations for each of them.

    Args:
    x (torch.Tensor): The input sequence embeddings with shape (batch_size, sequence_length, embedding_dim).
    raw_weights (torch.Tensor): The raw attention weights for each token in the sequence with shape (batch_size, sequence_length, sequence_length).
    weights (torch.Tensor): The scaled attention weights for each token in the sequence with shape (batch_size, sequence_length, sequence_length).
    y (torch.Tensor): The output sequence embeddings after applying self-attention with shape (batch_size, sequence_length, embedding_dim).
    q (torch.Tensor, optional): The query weight vectors used to compute the attention weights with shape (batch_size, sequence_length, embedding_dim).
    k (torch.Tensor, optional): The key weight vectors used to compute the attention weights with shape (batch_size, sequence_length, embedding_dim).
    v (torch.Tensor, optional): The value weight vectors used in the attention-weighted sum with shape (batch_size, sequence_length, embedding_dim).
    """

    fig_scale = 0.8
    fig_width = max(4, x.shape[1]) * fig_scale
    token_fig_height = 0.5 * x.shape[2]
    weight_fig_height = weights.shape[2]
    token_labels = [f"$T_{i}$" for i in range(x.shape[1])]
    weight_labels = [f"$W^T_{i}$" for i in range(weights.shape[1])]
    embedding_labels = [f"$E_{i}$" for i in range(x.shape[2])]
    weight_embedding_labels = [f"$W^E_{i}$" for i in range(weights.shape[2])]
    common_args = dict(
        annot=True,
        cbar=False,
    )

    plt.figure(figsize=(fig_width, token_fig_height))
    sns.heatmap(
        x[0, ::].T,
        xticklabels=token_labels,
        yticklabels=embedding_labels,
        **common_args,
    )
    plt.title("Input embedding values ($S_0$)")
    plt.show()

    if q is not None and k is not None and v is not None:
        for name, value in dict(q=q, k=k, v=v).items():
            plt.figure(figsize=(fig_width, token_fig_height))
            sns.heatmap(
                value[0, ::].T,
                xticklabels=[f"${name.upper()}_{i}$" for i in range(value.shape[1])],
                yticklabels=[f"$W^{name.upper()}_{i}$" for i in range(value.shape[2])],
                **common_args,
            )
            plt.title(f"{name.upper()} weight values ($S_0$)")
            plt.show()

    plt.figure(figsize=(fig_width, 0.5 * weight_fig_height))
    sns.heatmap(
        raw_weights[0, ::].T,
        xticklabels=weight_labels,
        yticklabels=weight_embedding_labels,
        **common_args,
    )
    plt.title("Raw weights for tokens ($S_0$)")
    plt.show()

    plt.figure(figsize=(fig_width, 0.5 * weight_fig_height))
    sns.heatmap(
        weights[0, ::].T,
        xticklabels=weight_labels,
        yticklabels=weight_embedding_labels,
        **common_args,
    )
    plt.title("Scaled weights for tokens ($S_0$)")
    plt.show()

    plt.figure(figsize=(fig_width, token_fig_height))
    sns.heatmap(
        y[0, ::].T,
        xticklabels=token_labels,
        yticklabels=embedding_labels,
        **common_args,
    )
    plt.title("Self-attention output ($S_0$)")
    plt.show()
