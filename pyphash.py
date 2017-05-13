import pHash
import sys
hash1 = pHash.imagehash( sys.argv[1] )
hash2 = pHash.imagehash( sys.argv[2] )
print 'Hamming distance: %d (%08x / %08x)' % ( pHash.hamming_distance( hash1, hash2 ), hash1, hash2 )

digest1 = pHash.image_digest( sys.argv[1], 1.0, 1.0, 180 )
digest2 = pHash.image_digest( sys.argv[2], 1.0, 1.0, 180 )
print ( pHash.crosscorr( digest1, digest2 ) )
