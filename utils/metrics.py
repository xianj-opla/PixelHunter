"""Security metrics calculation"""
import numpy as np
from typing import List, Dict

def calculate_far(frr_list: List[float], threshold: float) -> float:
    """Calculate False Acceptance Rate"""
    return np.mean([1 - frr for frr in frr_list])

def calculate_frr(far_list: List[float], threshold: float) -> float:
    """Calculate False Rejection Rate"""
    return np.mean(far_list)

def calculate_eer(far_list: List[float], frr_list: List[float]) -> float:
    """Calculate Equal Error Rate"""
    for i in range(len(far_list)):
        if abs(far_list[i] - frr_list[i]) < 0.01:
            return (far_list[i] + frr_list[i]) / 2
    return 0.0

def calculate_auc(scores: List[float], labels: List[int]) -> float:
    """Calculate Area Under Curve"""
    sorted_indices = np.argsort(scores)[::-1]
    tps = np.cumsum(np.array(labels)[sorted_indices])
    fps = np.cumsum(1 - np.array(labels)[sorted_indices])
    tpr = tps / tps[-1]
    fpr = fps / fps[-1]
    return np.trapz(tpr, fpr)
