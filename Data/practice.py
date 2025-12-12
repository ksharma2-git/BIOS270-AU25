import argparse
import numpy as np
import h5py

from query_bacteria_db import BacteriaDatabase  # assuming it's in same directory

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--database_path", type=str, required=True)
    parser.add_argument("--h5_path", type=str, required=True)
    parser.add_argument("--record_id", type=str, required=True)
    parser.add_argument("--metric", type=str, choices=["mean", "mean_mid"], required=True)
    parser.add_argument("--output_path", type=str, default="embeddings.npy")
    return parser.parse_args()

def main():
    args = parse_args()

    # 1. Connect to database and get protein IDs for this record
    db = BacteriaDatabase(args.database_path)
    protein_ids = db.get_protein_ids_from_record_id(args.record_id)
    db.close()

    if len(protein_ids) == 0:
        raise ValueError(f"No protein IDs found for record_id {args.record_id}")

    # 2. Open HDF5 file
    with h5py.File(args.h5_path, "r") as h5:
        
        h5_protein_ids = h5["protein_ids"][:]       # array of bytes/strings
        embeddings_ds = h5["embeddings"]            # shape: (N_total, 164)

        # Convert to normal Python strings if needed
        h5_protein_ids = [pid.decode("utf-8") if isinstance(pid, bytes) else pid
                          for pid in h5_protein_ids]

        # 3. Build dictionary: protein_id -> index
        id_to_index = {pid: idx for idx, pid in enumerate(h5_protein_ids)}

        # 4. Collect indices for the protein IDs belonging to this record
        indices = []
        for pid in protein_ids:
            if pid in id_to_index:
                indices.append(id_to_index[pid])
            else:
                
                pass

        if len(indices) == 0:
            raise ValueError("No matching protein IDs from this record were found in HDF5 file.")

        # 5. Get the embeddings matrix (N, D)
        indices = np.array(indices, dtype=int)
        emb_matrix = embeddings_ds[indices, :]  # shape (N, 164)

    # Save the full matrix as .npy
    np.save(args.output_path, emb_matrix)

    # 6. Compute metric if you want to print or store it
    if args.metric == "mean":
        metric_value = emb_matrix.mean(axis=0)      # shape (164,)
    elif args.metric == "mean_mid":
        N = emb_matrix.shape[0]
        mid = N // 2
        window = emb_matrix[max(0, mid - 5):min(N, mid + 5), :]
        metric_value = window.mean(axis=0)          # shape (164,)

    print(f"Saved embeddings matrix with shape {emb_matrix.shape} to {args.output_path}")
    print(f"Metric ({args.metric}) vector shape: {metric_value.shape}")

if __name__ == "__main__":
    main()